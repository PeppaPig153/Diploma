package etu.moevm.vkr.ui.Fragment

import android.content.pm.PackageManager
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.core.content.ContextCompat
import androidx.navigation.NavController
import androidx.navigation.findNavController
import androidx.navigation.fragment.findNavController
import com.arellomobile.mvp.MvpAppCompatFragment
import etu.vt.trpo_android.R
import etu.moevm.vkr.present.view.StartView
import etu.moevm.vkr.util.PermissionManager


class StartFragment: MvpAppCompatFragment(), StartView {

    override fun onCreate(savedInstanceState: Bundle?) {
        this.retainInstance = true
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        var view = inflater.inflate(R.layout.start_fragment, container, false)
        val navCon : NavController = this.findNavController()

        val startButton = view.findViewById<Button>(R.id.start_button)
        startButton.setOnClickListener {
            navCon.navigate(R.id.currentProjectFragment)
        }

        return view

    }

}