package etu.moevm.vkr.model

data class CardModel(var title: String)

object Supplier {
    val Titles = listOf<CardModel>(CardModel("1"), CardModel("2"))
}