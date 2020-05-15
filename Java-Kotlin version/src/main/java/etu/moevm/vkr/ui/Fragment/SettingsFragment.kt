package etu.moevm.vkr.ui.Fragment

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import com.arellomobile.mvp.MvpAppCompatFragment
import etu.vt.trpo_android.R
import etu.moevm.vkr.present.view.SettingsView


class SettingsFragment: MvpAppCompatFragment(), SettingsView {
    override fun onCreate(savedInstanceState: Bundle?) {
        this.retainInstance = true
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        val view = inflater.inflate(R.layout.settings_fragment, container, false)
        val navCon : NavController = this.findNavController()

        val nextButton = view.findViewById<Button>(R.id.next_set_btn)

        nextButton.setOnClickListener {
            navCon.navigate(R.id.connectionServertFragment)
        }

        return view
    }
}