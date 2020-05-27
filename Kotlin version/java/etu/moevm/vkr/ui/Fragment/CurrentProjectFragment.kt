package etu.moevm.vkr.ui.Fragment

import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageButton
import android.widget.ImageView
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.core.content.ContextCompat
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.arellomobile.mvp.MvpAppCompatFragment
import com.arellomobile.mvp.presenter.InjectPresenter
import etu.moevm.vkr.adapter.ListModelAdapter
import etu.moevm.vkr.model.ListModel
import etu.moevm.vkr.model.StructScanner
import etu.moevm.vkr.present.presenter.CurrentProjectPresenter
import etu.moevm.vkr.R
import etu.moevm.vkr.present.view.CurrentProjectView
import etu.moevm.vkr.repository.PictureRepositoryProvider
import etu.moevm.vkr.ui.Activity.MainActivity
import etu.moevm.vkr.ui.Fragment.PictureFragment.SingleBitmap.mbitmap
import etu.moevm.vkr.util.PermissionManager
import org.opencv.android.BaseLoaderCallback
import org.opencv.android.LoaderCallbackInterface
import org.opencv.android.OpenCVLoader
import org.opencv.core.Mat


class CurrentProjectFragment: MvpAppCompatFragment(), CurrentProjectView {

    val pictureRepository = PictureRepositoryProvider.providePictureRepository()
    private lateinit var mListModelAdapter: ListModelAdapter
    private lateinit var listRecyclerView: RecyclerView

    object SingleBitmap{
        var mbitmap: Bitmap? = null
    }

    @InjectPresenter
    lateinit var mCurrentProjectPresenter: CurrentProjectPresenter


    override fun onResume() {
        super.onResume()
        mListModelAdapter = ListModelAdapter(MainActivity.StructList.list)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        if (savedInstanceState != null)
            mbitmap = savedInstanceState.getParcelable("mbitmap")
        super.onCreate(savedInstanceState)
        retainInstance = true //save state fragment
        mListModelAdapter = ListModelAdapter(MainActivity.StructList.list)
    }

    @RequiresApi(Build.VERSION_CODES.Q)
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        val view = inflater.inflate(R.layout.current_project_fragment, container, false)
        val navCon : NavController = this.findNavController()
        val newPhotoButton = view.findViewById<ImageButton>(R.id.new_photo_btn)
        val nextButton = view.findViewById<Button>(R.id.next_cp_btn)
        listRecyclerView = view.findViewById(R.id.recycler_view)

        listRecyclerView.apply {
            layoutManager = LinearLayoutManager(activity)
            adapter = mListModelAdapter
        }

        newPhotoButton.setOnClickListener {
            if (ContextCompat.checkSelfPermission(requireContext(),
                    android.Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED){
                mCurrentProjectPresenter.clickTakePicture(this)
            }
            else
                PermissionManager().requestPermissionsCamera(this)
        }

        nextButton.setOnClickListener {
                if(MainActivity.StructList.list.isEmpty()){
                Toast.makeText(context, "Добавьте хотя бы один трафарет в проект!", Toast.LENGTH_LONG).show()
            }
            else{
                navCon.navigate(R.id.settingsFragment)
            }
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

    private  val lastVisibleItemPosition: Int
        get () = LinearLayoutManager(context).findLastVisibleItemPosition ()

}