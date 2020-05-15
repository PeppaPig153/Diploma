package etu.moevm.vkr.present.presenter


import android.annotation.SuppressLint
import android.app.Activity
import android.app.ActivityOptions
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Matrix
import android.media.ExifInterface
import android.media.MediaScannerConnection
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.util.Log
import android.widget.ImageView
import androidx.core.content.FileProvider
import androidx.navigation.NavController
import androidx.navigation.NavHostController
import androidx.navigation.findNavController
import androidx.navigation.fragment.NavHostFragment.findNavController
import com.arellomobile.mvp.InjectViewState
import com.arellomobile.mvp.MvpAppCompatFragment
import com.arellomobile.mvp.MvpPresenter
import etu.moevm.vkr.present.view.CurrentProjectView
import etu.moevm.vkr.present.view.PictureView
import etu.moevm.vkr.repository.PictureRepository
import etu.moevm.vkr.ui.Activity.MainActivity
import etu.moevm.vkr.ui.Fragment.CurrentProjectFragment
import etu.moevm.vkr.ui.Fragment.PictureFragment
import etu.moevm.vkr.util.DecodeBitmapFromInputStream
import etu.moevm.vkr.util.PermissionManager
import etu.moevm.vkr.util.getExifAngle
import etu.vt.trpo_android.R
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.asRequestBody
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.io.*
import java.text.SimpleDateFormat
import java.util.*


@InjectViewState
class CurrentProjectPresenter : MvpPresenter<CurrentProjectView>() {
    lateinit var mainView: PictureView
    private lateinit var currentPhotoPath: String
    private val CAMERA_REQUEST_CODE = 1
    private val OPEN_PICTURE_REQUEST_CODE = 2
    private val MY_CAMERA_PERMISSION_REQUEST = 100
    private val WRITE_READ_FILE_PERMISSION_REQUEST = 102
    private val WRITE_READ_MEDIA_FILE_PERMISSION_REQUEST = 103
    private val INTERNET_PERMISSION_REQUEST = 104
    private var photoFile: File? = null
    private var photoFilePath: String = ""
    private var outputFile: Uri? = null

    fun clickTakePicture(fragment: MvpAppCompatFragment){

        PermissionManager().requestPermissionsCamera(fragment)
        val file = createImageFile(fragment)
        outputFile = FileProvider.getUriForFile(
            fragment.requireContext(),
            fragment.requireContext().applicationContext.packageName + ".provider", file
        )
        photoFilePath = file.path
        val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        intent.putExtra(MediaStore.EXTRA_OUTPUT, outputFile)
        fragment.startActivityForResult(
            intent,
            CAMERA_REQUEST_CODE,
            ActivityOptions.makeSceneTransitionAnimation(fragment.requireActivity()).toBundle()
        )
    }

    fun onActivityResultCamera(
        requestCode: Int,
        resultCode: Int,
        data: Intent?,
        fragment: MvpAppCompatFragment
    ) {
        val imViewHeight = 432//imView.height
        val imViewWidth = 333// imView.width
        Log.d("imView width is ", imViewWidth.toString())
        Log.d("imView height is ", imViewHeight.toString())

        when (requestCode) {
            CAMERA_REQUEST_CODE -> {
                if (resultCode == Activity.RESULT_OK) {
                    //if (data != null && data.hasExtra("data")) {
                    try {
                        var stream = fragment.requireContext().contentResolver.openInputStream(outputFile!!)
                        if (stream == null )
                            Log.d("Stream null +++++", "imstream")
                        val buffer = BufferedInputStream(stream!!)

                        val out  = DecodeBitmapFromInputStream().run {
                            decodeSampledBitmapFromInputStream(buffer, imViewWidth, imViewHeight)
                        }
                        if (out == null )
                            Log.d("OUT null +++++", "OUT NULL")
                        stream.close()

                        val matrix = Matrix()
                        stream = fragment.requireContext().contentResolver.openInputStream(outputFile!!)
                        matrix.postRotate(getExifAngle(stream!!, fragment))


                        stream.close()
                        buffer.close()


                        //PictureFragment.SingleBitmap.mbitmap =
                        CurrentProjectFragment.SingleBitmap.mbitmap =
                            Bitmap.createBitmap(out!!, 0, 0, out.width, out.height, matrix, true)
                        Log.d("mbitmap width is ", CurrentProjectFragment.SingleBitmap.mbitmap?.height.toString())
                        Log.d("mbitmap height is ", CurrentProjectFragment.SingleBitmap.mbitmap?.width.toString())

                        //imView.setImageBitmap(PictureFragment.SingleBitmap.mbitmap)

//                        val bundle: Bundle? = Bundle()
//                        bundle?.putParcelable("mbitmap", bitmap)
//                        val bun = Bundle().putParcelable("mbitmap", bitmap)
//                        Log.d("Bundle", bundle.toString())
                        findNavController(fragment).navigate(R.id.contoursFragment)

                    } catch (e: IOException) {
                        Log.d("Can`t close streams", "Can`t close streams: $e")
                    }
                    catch (e: FileNotFoundException) {
                        Log.d("Not found file", "Image file not found: $e")
                    }
                    catch (e: Exception) {
                        Log.d("clickTakePicture", e.toString())
                    }

                } else if (resultCode == Activity.RESULT_CANCELED) {
                    Log.d("CAMERA_REQUEST_CODE", "Canceled")
                }

            }


            OPEN_PICTURE_REQUEST_CODE -> {
                if(resultCode == Activity.RESULT_OK && data != null) {
                    try {
                        val imageUri = data.data
                        Log.d("imageUri", data.data.toString())

                        photoFilePath = imageUri?.path!!
                        var imageStream = fragment.requireContext().contentResolver.openInputStream(imageUri)
                        val buffer = BufferedInputStream(imageStream!!)

                        val out: Bitmap? = DecodeBitmapFromInputStream()
                            .decodeSampledBitmapFromInputStream(buffer, imViewWidth, imViewHeight)
                        if (out == null ) {
                            Log.d("out null +", "out")
                            viewState.pushToast("Не смог преобразовать фото")
                        }

                        try {
                            imageStream.close()
                            buffer.close()
                        }catch (e: IOException){
                            Log.d("Streams close", "Can`t close image streams")
                        }

                        imageStream = fragment.requireContext().contentResolver.openInputStream(imageUri)
                        if (imageStream == null )
                            Log.d("imageStream second null +", "imstream")

                        val matrix = Matrix()
                        matrix.postRotate(getExifAngle(imageStream!!, fragment))
                        imageStream.close()

                        PictureFragment.SingleBitmap.mbitmap =
                            Bitmap.createBitmap(out!!, 0, 0, out.width, out.height, matrix, true)

                        Log.d("mbitmap width is ", PictureFragment.SingleBitmap.mbitmap?.height.toString())
                        Log.d("mbitmap height is ", PictureFragment.SingleBitmap.mbitmap?.width.toString())
                        Log.d("selectedImage", PictureFragment.SingleBitmap.mbitmap.toString())

                       // imView.setImageBitmap(PictureFragment.SingleBitmap.mbitmap)


                    } catch (e: IOException) {
                        Log.d("Can`t close streams", "Can`t close streams: $e")
                    }
                    catch (e: FileNotFoundException) {
                        Log.d("Not found file", "Image file not found: $e")
                    }
                    catch (e: Exception) {
                        Log.d("clickOpenPicture", e.toString())
                    }
                }
                else if (resultCode == Activity.RESULT_CANCELED) {
                    Log.d("CAMERA_REQUEST_CODE", "Canceled")
                }
            }
        }
    }

    @SuppressLint("SimpleDateFormat")
    @Throws(IOException::class)
    fun createImageFile(fragment: MvpAppCompatFragment): File {
        // Create an image file name
        val file: File
        val timeStamp: String = SimpleDateFormat("yyyyMMdd_HHmmss").format(Date())
        Log.d("TimeStamp is ", timeStamp)
        val storageDir = fragment.context?.getExternalFilesDir(Environment.DIRECTORY_PICTURES)
        Log.d("mkdir dir is ", storageDir!!.exists().toString())

        if (!storageDir.exists() && storageDir.isDirectory) {
            try {
                storageDir.mkdir()
            } catch (ex: SecurityException) {
                val errorMessage = "Не удалось создать папку и сохранить файл!"
                viewState.pushToast(errorMessage)
            }
        }
        file = File.createTempFile(
            "JPEG_${timeStamp}_", /* prefix */
            ".jpg", /* suffix */
            storageDir /* directory */
        ).apply {
            // Save a file: path for use with ACTION_VIEW intents
            currentPhotoPath = absolutePath
        }


        Log.d("Storage dir is ", storageDir.toString())
        return file
    }

}