package etu.moevm.vkr.util

import android.media.ExifInterface
import android.os.Build
import android.util.Log
import com.arellomobile.mvp.MvpAppCompatFragment
import java.io.InputStream

fun getExifAngle(path: InputStream, fragment: MvpAppCompatFragment): Float {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        PermissionManager().requestPermissionsOpenFile(fragment)
    }
    var angle = 0
    try {
        val ei = ExifInterface(path)
        val orientation: Int = ei.getAttributeInt(
            ExifInterface.TAG_ORIENTATION,
            ExifInterface.ORIENTATION_UNDEFINED
        )
        when (orientation) {
            ExifInterface.ORIENTATION_ROTATE_90 -> angle = 90
            ExifInterface.ORIENTATION_ROTATE_180 -> angle = 180
            ExifInterface.ORIENTATION_ROTATE_270 -> angle = 270
        }
    } catch (e: java.lang.Exception) {
        Log.d("getExifAngle", e.toString())
    }
    return angle.toFloat()
}