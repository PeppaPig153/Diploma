package etu.moevm.vkr.ui.Fragment

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.annotation.StringRes
import com.arellomobile.mvp.MvpAppCompatFragment
import etu.moevm.vkr.R
import etu.moevm.vkr.present.view.AboutView

class AboutFragment: MvpAppCompatFragment(), AboutView {

    override fun onCreate(savedInstanceState: Bundle?) {
        this.retainInstance = true
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        val view = inflater.inflate(R.layout.about_fragment, container, false)
        val aboutText = view.findViewById<TextView>(R.id.text_about)
        aboutText.text = resources.getString(R.string.about)
        return view
    }
}