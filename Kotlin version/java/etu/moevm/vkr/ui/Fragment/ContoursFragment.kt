package etu.moevm.vkr.ui.Fragment

import android.graphics.Bitmap
import android.media.Image
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageButton
import android.widget.ImageView
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import com.arellomobile.mvp.MvpAppCompatFragment
import com.arellomobile.mvp.presenter.InjectPresenter
import etu.moevm.vkr.model.StructScanner
import etu.moevm.vkr.present.presenter.ContoursPresenter
import etu.moevm.vkr.present.presenter.PicturePresenter
import etu.moevm.vkr.R
import etu.moevm.vkr.present.view.ContoursView
import etu.moevm.vkr.ui.Activity.MainActivity
import java.sql.Struct


class ContoursFragment: MvpAppCompatFragment(), ContoursView {

    @InjectPresenter
    lateinit var mPicturePresenter: ContoursPresenter
    lateinit var img_view: ImageView
    var imBitmap: Bitmap? = null
    private var structGetting: StructScanner? = null
    private lateinit var yesButton: ImageButton
    private lateinit var noButton: ImageButton

    override fun onCreate(savedInstanceState: Bundle?) {
        structGetting = arguments?.getParcelable("struct")
        this.retainInstance = true
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        val view = inflater.inflate(R.layout.contours_fragment, container, false)
        val navCon : NavController = this.findNavController()

        img_view = view.findViewById(R.id.img_view)

        if(CurrentProjectFragment.SingleBitmap.mbitmap != null) {
            showPicture(CurrentProjectFragment.SingleBitmap.mbitmap)
        }

        yesButton = view.findViewById(R.id.yes_btn)
        noButton = view.findViewById(R.id.no_btn)

        yesButton.setOnClickListener {
            structGetting?.let { it1 -> MainActivity.StructList.list.add(it1) }
            navCon.navigate(R.id.currentProjectFragment)
        }

        noButton.setOnClickListener {
            navCon.navigate(R.id.currentProjectFragment)
        }

        return view
    }

    override fun showPicture(bitmap: Bitmap?) {
        if (bitmap != null) {
            img_view.setImageBitmap(bitmap)
        }
    }
}