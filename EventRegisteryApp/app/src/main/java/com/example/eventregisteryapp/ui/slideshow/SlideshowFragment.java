package com.example.eventregisteryapp.ui.slideshow;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;
import com.example.eventregisteryapp.R;
import com.example.eventregisteryapp.databinding.FragmentSlideshowBinding;
import org.jetbrains.annotations.NotNull;

import static android.content.ContentValues.TAG;

public class SlideshowFragment extends Fragment {

    private SlideshowViewModel slideshowViewModel;
private FragmentSlideshowBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
            ViewGroup container, Bundle savedInstanceState) {
        slideshowViewModel =
                new ViewModelProvider(this).get(SlideshowViewModel.class);


    binding = FragmentSlideshowBinding.inflate(inflater, container, false);
    View root = binding.getRoot();

        final TextView textView = binding.textSlideshow;
        slideshowViewModel.getText().observe(getViewLifecycleOwner(), new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                textView.setText(s);
            }
        });
        return root;
    }

@Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
        Log.i(TAG, "Zostałęm zniszczony");
    }

    @Override
    public void onCreate(@Nullable @org.jetbrains.annotations.Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.i(TAG, "Zostałęm Stworzony");
    }

    @Override
    public void onViewCreated(@NonNull @NotNull View view, @Nullable @org.jetbrains.annotations.Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        Log.i(TAG, "Widok został utworzony");
    }

    @Override
    public void onViewStateRestored(@Nullable @org.jetbrains.annotations.Nullable Bundle savedInstanceState) {
        super.onViewStateRestored(savedInstanceState);
        Log.i(TAG, "Widok został wczytany");
    }

    @Override
    public void onStart() {
        super.onStart();
        Log.i(TAG, "Widok wystartował");
    }

    @Override
    public void onResume() {
        super.onResume();
        Log.i(TAG, "Widok został wznowiony");
    }

    @Override
    public void onPause() {
        super.onPause();
        Log.i(TAG, "Widok został zapałzowany");
    }

    @Override
    public void onStop() {
        super.onStop();
        Log.i(TAG, "Widok został zatrzymany");
    }

    @Override
    public void onSaveInstanceState(@NonNull @NotNull Bundle outState) {
        super.onSaveInstanceState(outState);
        Log.i(TAG, "Została zapisana instancja widoku");
    }
}