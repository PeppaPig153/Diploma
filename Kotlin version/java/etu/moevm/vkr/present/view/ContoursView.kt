package etu.moevm.vkr.present.view

import android.graphics.Bitmap
import com.arellomobile.mvp.MvpView

interface ContoursView: MvpView {
    fun showPicture(bitmap: Bitmap?)
}