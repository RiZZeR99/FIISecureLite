package com.license.antivirus.utils;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPool {
    private static  ThreadPool instance;
    private ExecutorService pool;
    private ThreadPool(){
        pool = Executors.newCachedThreadPool();
    }

    public static ThreadPool getInstance(){
        if(instance == null){
            instance = new ThreadPool();
        }
        return instance;
    }

    public void execute(Runnable action){
        pool.submit(action);
    }

    public void sleep(int milliseconds){
        try {
            Thread.sleep(milliseconds);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
