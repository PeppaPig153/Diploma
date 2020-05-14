package etu.moevm.vkr.present.view

import android.graphics.Bitmap
import com.arellomobile.mvp.MvpView

interface PictureView: MvpView {
    fun showPicture(bitmap: Bitmap?)
    fun pushToast(str: String)
}