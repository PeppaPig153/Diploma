package etu.moevm.vkr.ui.Fragment

import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageButton
import android.widget.ImageView
import android.widget.Toast
import androidx.core.content.ContextCompat
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import com.arellomobile.mvp.MvpAppCompatFragment
import com.arellomobile.mvp.presenter.InjectPresenter
import etu.moevm.vkr.present.presenter.CurrentProjectPresenter
import etu.vt.trpo_android.R
import etu.moevm.vkr.present.view.CurrentProjectView
import etu.moevm.vkr.repository.PictureRepositoryProvider
import etu.moevm.vkr.ui.Fragment.PictureFragment.SingleBitmap.mbitmap
import etu.moevm.vkr.util.PermissionManager


class CurrentProjectFragment: MvpAppCompatFragment(), CurrentProjectView {

    val pictureRepository = PictureRepositoryProvider.providePictureRepository()

    object SingleBitmap{
        var mbitmap: Bitmap? = null
    }

    @InjectPresenter
    lateinit var mCurrentProjectPresenter: CurrentProjectPresenter


    override fun onCreate(savedInstanceState: Bundle?) {
        if (savedInstanceState != null)
            mbitmap = savedInstanceState.getParcelable("mbitmap")
        super.onCreate(savedInstanceState)
        retainInstance = true //save state fragment
//        mCurrentProjectPresenter.onShowPicture()
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        val view = inflater.inflate(R.layout.current_project_fragment, container, false)
        val navCon : NavController = this.findNavController()
        val newPhotoButton = view.findViewById<ImageButton>(R.id.new_photo_btn)
        val nextButton = view.findViewById<Button>(R.id.next_cp_btn)

        newPhotoButton.setOnClickListener {
            if (ContextCompat.checkSelfPermission(requireContext(),
                    android.Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED){
                mCurrentProjectPresenter.clickTakePicture(this)
            }
            else
                PermissionManager().requestPermissionsCamera(this)
        }

        nextButton.setOnClickListener {
            navCon.navigate(R.id.settingsFragment)
        }

        return view
    }


    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        mCurrentProjectPresenter.onActivityResultCamera(requestCode, resultCode, data,this)
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        //mCurrentProjectPresenter.requestPermissionsResult(requestCode, permissions, grantResults, this)
    }

    override fun pushToast(str: String) {
        Toast.makeText(context, str, Toast.LENGTH_SHORT).show()
    }


}