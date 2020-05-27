package etu.moevm.vkr.present.view

import android.graphics.Bitmap
import com.arellomobile.mvp.MvpView

interface CurrentProjectView: MvpView {
    fun pushToast(str: String)
}