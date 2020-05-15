package etu.moevm.vkr.ui.Activity

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.NavController
import androidx.navigation.Navigation
import androidx.navigation.findNavController
import etu.moevm.vkr.ui.Fragment.PictureFragment
import etu.vt.trpo_android.R


class MainActivity : AppCompatActivity() {

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

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onSupportNavigateUp(): Boolean {
        return findNavController(R.id.navHostMain).navigateUp()
    }





}
