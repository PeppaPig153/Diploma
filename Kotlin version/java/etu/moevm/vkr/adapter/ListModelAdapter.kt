package etu.moevm.vkr.adapter

import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageButton
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import etu.moevm.vkr.model.ListModel
import etu.moevm.vkr.model.StructScanner
import etu.moevm.vkr.R
import etu.moevm.vkr.ui.Activity.MainActivity

class ListModelAdapter(private val list: MutableList<StructScanner>):
    RecyclerView.Adapter<ListModelAdapter.ListModelViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ListModelViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val listItemView = inflater.inflate(R.layout.list_item, parent, false)
        return ListModelViewHolder(listItemView)
    }

    override fun getItemCount(): Int = list.size

    override fun onBindViewHolder(holder: ListModelViewHolder, position: Int) {
        val listModel: StructScanner = list[position]
        holder.bind(listModel)
        val counter = holder.counter
        val plusButton = holder.plusButton
        val minusButton = holder.minusButton

        plusButton.setOnClickListener {
            counter.text = plusCounter(counter.text.toString())
            listModel.counter = counter.text.toString().toInt()
            Log.d("ListCounter", MainActivity.StructList.list.toString())
        }
        minusButton.setOnClickListener {
            counter.text = minusCounter(counter.text.toString())
            listModel.counter = counter.text.toString().toInt()
            Log.d("ListCounter", MainActivity.StructList.list.toString())
        }
    }

    private fun plusCounter(counter: String): String {
        var count = counter.toInt()
        if (count == Int.MAX_VALUE)
            count = 0
        else
            count++
        return count.toString()
    }

    private fun minusCounter(counter: String): String {
        var count = counter.toInt()
        if (count == 1)
            count = 1
        else
            count--
        return count.toString()
    }

    class ListModelViewHolder(listItemView : View) :
        RecyclerView.ViewHolder(listItemView) {
        private var mCardTitle : TextView? = null
        private var mCounter : TextView? = null

        val counter = listItemView.findViewById<TextView>(R.id.counter)
        val plusButton = listItemView.findViewById<ImageButton>(R.id.card_plus)
        val minusButton = listItemView.findViewById<ImageButton>(R.id.card_minus)

        init {
            mCardTitle = itemView.findViewById(R.id.cardTitle)
            mCounter = itemView.findViewById(R.id.counter)
        }

        fun bind(model: StructScanner) {
            mCardTitle?.text = model.title
            mCounter?.text = model.counter.toString()
        }
    }


}