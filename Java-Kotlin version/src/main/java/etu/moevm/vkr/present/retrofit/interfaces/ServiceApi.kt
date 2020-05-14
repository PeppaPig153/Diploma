package etu.moevm.vkr.present.retrofit.interfaces

import okhttp3.MultipartBody
import okhttp3.OkHttpClient
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import retrofit2.converter.jackson.JacksonConverterFactory
import retrofit2.http.*
import java.util.concurrent.TimeUnit

interface ServiceApi {

    /**
     *   Method for sending POST request to service by path (baseUrl + @POST(value)) and receiving
     *   JSON data
     *   @param {@Body ImageRequest} Data class contained in request which converting to JSON
     *   @return {Observable<ImageResult>}
     **/
    @Multipart
    @POST("/api/picture")
    fun postPictureToServerApi(
        @Part imageRequestJson: MultipartBody.Part): Call<ResponseBody>

    /**
     *   Singleton to get Retrofit object
     **/
    companion object Factory{
        private const val baseUrl = "https://polar-taiga-40515.herokuapp.com"
        fun createService(): ServiceApi{
            val httpClient: OkHttpClient.Builder = OkHttpClient.Builder()
                .callTimeout(2, TimeUnit.MINUTES)
                .connectTimeout(2, TimeUnit.MINUTES)
                .readTimeout(2, TimeUnit.MINUTES)
                .writeTimeout(2, TimeUnit.MINUTES)

            val retrofit = Retrofit.Builder()
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .addConverterFactory(JacksonConverterFactory.create())
                .client(httpClient.build())
                .baseUrl(baseUrl)
                .build()

            return retrofit.create(ServiceApi::class.java)
        }
    }


}