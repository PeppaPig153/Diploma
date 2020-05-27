package etu.moevm.vkr.ui.Fragment

import android.os.Bundle
import android.os.Environment
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.navigation.NavController
import androidx.navigation.fragment.findNavController
import com.arellomobile.mvp.MvpAppCompatFragment
import com.arellomobile.mvp.presenter.InjectPresenter
import etu.moevm.vkr.R
import etu.moevm.vkr.present.presenter.SettingsPresenter
import etu.moevm.vkr.present.view.SettingsView
import etu.moevm.vkr.ui.Activity.MainActivity
import etu.moevm.vkr.util.SVGwriter
import etu.moevm.vkr.util.ScannerImage



class SettingsFragment: MvpAppCompatFragment(), SettingsView {
    @InjectPresenter
    lateinit var mSettingsPresenter: SettingsPresenter

    override fun onCreate(savedInstanceState: Bundle?) {
        retainInstance = true
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?  ): View? {
        val view = inflater.inflate(R.layout.settings_fragment, container, false)
        val navCon : NavController = this.findNavController()
        val nextButton = view.findViewById<Button>(R.id.next_set_btn)
        val project_name = view.findViewById<EditText>(R.id.project_name_input)
        val square_size = view.findViewById<EditText>(R.id.square_size_input)
        val length = view.findViewById<EditText>(R.id.length_input)
        val width = view.findViewById<EditText>(R.id.width_input)
        var flag = true

        nextButton.setOnClickListener {
            Log.d("Input", MainActivity.StructList.list.toString())
            flag = true
            if(project_name.text.isEmpty()){
                project_name.setError("Пожалуйста, введите название проекта!")
                flag = false;
            }
            if(square_size.text.isEmpty()){
                square_size.setError("Пожалуйста, введите длину стороны установочного квадрата!")
                flag = false;
            }
            if(length.text.isEmpty()){
                length.setError("Пожалуйста, введите длину контейнера!")
                flag = false;
            }
            if(width.text.isEmpty()){
                width.setError("Пожалуйста, введите ширину контейнера!")
                flag = false;
            }

                if (mSettingsPresenter.hasConnection(context) == true) {
                    if(flag) {
                        val params = ScannerImage().resizeContours(
                            MainActivity.StructList.list,
                            square_size.text.toString().toDouble(),
                            width.text.toString().toDouble(),
                            length.text.toString().toDouble()
                        )
                        Log.d("SIZE_2", " width = $width, height = $length")
                        val storageDir =
                            context?.getExternalFilesDir(Environment.DIRECTORY_PICTURES)?.absolutePath
                        val svg_file = SVGwriter.write(
                            MainActivity.StructList.list,
                            params[0],
                            params[1],
                            params[2],
                            params[3],
                            params[4].toInt(),
                            project_name.text.toString(),
                            storageDir
                        )
                        val bundle: Bundle? = Bundle()
                        bundle?.putString("svg_file", svg_file)
                        navCon.navigate(R.id.SVGnestFragment, bundle)
                    }
                }
                else{
                    Toast.makeText(context, "Нет подключения к Интернету!", Toast.LENGTH_LONG).show()
                }
        }

        return view
    }
}