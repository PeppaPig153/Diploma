package etu.moevm.vkr.model

import com.fasterxml.jackson.annotation.JsonProperty
import java.io.File

data class ImageRequest (
    //@SerializedName("arrPicture")
    //@Expose
    @JsonProperty("arrPicture")
    var arrPicture: File
)

//data class ImageResult (val id: Int, val type: String, val name: String, val probability: Double)
data class ImageResult (
    //@SerializedName("content")
    //@Expose
    @JsonProperty("content")
    var content: String,
    //@SerializedName("arrPicture")
    //@Expose
    @JsonProperty("arrPicture")
    var arrPicture: File
)