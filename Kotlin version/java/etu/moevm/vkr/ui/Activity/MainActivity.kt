package etu.moevm.vkr.ui.Activity

import android.annotation.TargetApi
import android.content.ActivityNotFoundException
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import android.webkit.ValueCallback
import android.webkit.WebChromeClient
import android.webkit.WebView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.app.ActivityCompat.startActivityForResult
import androidx.navigation.NavController
import androidx.navigation.findNavController
import etu.moevm.vkr.model.StructScanner
import etu.moevm.vkr.ui.Fragment.PictureFragment
import etu.moevm.vkr.R
import org.opencv.android.OpenCVLoader


class MainActivity : AppCompatActivity() {

    object StructList{
        var list: MutableList<StructScanner> = mutableListOf()
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        val inflater = menuInflater
        inflater.inflate(R.menu.options_menu, menu)
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        val navCon : NavController = findNavController(R.id.navHostMain)
        var bundleNav: Bundle? = null
        when(item.itemId){
            R.id.action_main_page ->{
                navCon.navigate(R.id.startFragment, null)
                return true
            }

            R.id.action_instruction ->{
                return if (PictureFragment.SingleBitmap.mbitmap != null) {
                    bundleNav?.putParcelable("mbitmap", PictureFragment.SingleBitmap.mbitmap)
                    navCon.navigate(R.id.instructionsFragment, bundleNav)
                    true
                }else {
                    navCon.navigate(R.id.instructionsFragment, bundleNav)
                    true
                }
            }

            R.id.action_about ->{
                return if (PictureFragment.SingleBitmap.mbitmap != null) {
                    bundleNav?.putParcelable("mbitmap", PictureFragment.SingleBitmap.mbitmap)
                    navCon.navigate(R.id.aboutFragment, bundleNav)
                    true
                }else {
                    navCon.navigate(R.id.aboutFragment, bundleNav)
                    true
                }
            }
        }
        return super.onOptionsItemSelected(item)
    }


    override fun onCreate(savedInstanceState: Bundle?) {
        //вместо метода OnResume в CurrentProjectFragment
        OpenCVLoader.initDebug()
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onSupportNavigateUp(): Boolean {
        return findNavController(R.id.navHostMain).navigateUp()
    }

}

