package etu.moevm.vkr.model

import android.R.attr.name
import android.os.Parcel
import android.os.Parcelable
import kotlinx.android.parcel.Parcelize
import kotlinx.android.parcel.RawValue
import org.opencv.core.MatOfPoint
import kotlin.properties.Delegates


@Parcelize
data class StructScanner (
    var title: String,
    var pathToFile: String?,
    var counter: Int,
    var square: Double?,
    var length: Double?,
    var arrPoint: ArrayList<DoubleArray>? ): Parcelable {
}