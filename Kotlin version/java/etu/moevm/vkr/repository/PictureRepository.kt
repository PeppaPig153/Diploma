package etu.moevm.vkr.repository

import etu.moevm.vkr.present.retrofit.interfaces.ServiceApi
import okhttp3.MultipartBody
import okhttp3.ResponseBody
import retrofit2.Call

/**
 *   Picture repository for action with service
 **/
class PictureRepository(val apiServiceApi: ServiceApi) {

    /**
     *   Method for sending request and response data from service
     *   @param {NnpiServiceApi} Interface for service
     *   @return {Observable<ImageResult>}
     **/
    fun sendPictureForResult(imageRequestJson: MultipartBody.Part): Call<ResponseBody> {
        return apiServiceApi.postPictureToServerApi(imageRequestJson)
    }



}