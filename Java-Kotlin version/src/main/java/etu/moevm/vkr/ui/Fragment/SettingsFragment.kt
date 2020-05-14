package etu.moevm.vkr.ui.Fragment

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.arellomobile.mvp.MvpAppCompatFragment
import etu.vt.trpo_android.R
import etu.moevm.vkr.present.view.SettingsView

class SettingsFragment: MvpAppCompatFragment(), SettingsView {

    override fun onCreate(savedInstanceState: Bundle?) {
        this.retainInstance = true
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        return inflater.inflate(R.layout.settings_fragment, container, false)
    }
}