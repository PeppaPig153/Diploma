package etu.moevm.vkr.repository

import etu.moevm.vkr.present.retrofit.interfaces.ServiceApi

object PictureRepositoryProvider{

    /**
     *   Provider (Singleton object) for create Picture Repository
     **/

    fun providePictureRepository(): PictureRepository{
        return PictureRepository(ServiceApi.createService())
    }
}