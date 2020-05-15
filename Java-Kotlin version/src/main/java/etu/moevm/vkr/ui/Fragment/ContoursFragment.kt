package etu.moevm.vkr.ui.Fragment

import android.graphics.Bitmap
import android.media.Image
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import com.arellomobile.mvp.MvpAppCompatFragment
import com.arellomobile.mvp.presenter.InjectPresenter
import etu.moevm.vkr.present.presenter.ContoursPresenter
import etu.moevm.vkr.present.presenter.PicturePresenter
import etu.vt.trpo_android.R
import etu.moevm.vkr.present.view.ContoursView


class ContoursFragment: MvpAppCompatFragment(), ContoursView {

    @InjectPresenter
    lateinit var mPicturePresenter: ContoursPresenter
    lateinit var img_view: ImageView
    var imBitmap: Bitmap? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        this.retainInstance = true
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        val view = inflater.inflate(R.layout.contours_fragment, container, false)
        img_view = view.findViewById<ImageView>(R.id.img_view)
        if(CurrentProjectFragment.SingleBitmap.mbitmap != null) {
            Log.d("imBitmap", CurrentProjectFragment.SingleBitmap.mbitmap.toString())
            showPicture(CurrentProjectFragment.SingleBitmap.mbitmap)
        }
        return view
    }

    override fun showPicture(bitmap: Bitmap?) {
        if (bitmap != null) {
            img_view.setImageBitmap(bitmap)
        }
    }
}