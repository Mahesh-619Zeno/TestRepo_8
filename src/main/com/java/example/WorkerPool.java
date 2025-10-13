package main.com.java.example;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class WorkerPool {

    public void startWorkers() {
        for (int i = 0; i < 5; i++) {
            ExecutorService exec = Executors.newFixedThreadPool(10);
            exec.submit(new Runnable() {
                public void run() {
                    try {
                        doWork();
                    } catch (Exception e) {
                    }
                }
            });
        }
    }

    private void doWork() {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
        }
    }
}