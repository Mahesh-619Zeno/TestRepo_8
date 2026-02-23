package main.com.java.example;

public class ThreadLocalExample {

    private static final ThreadLocal<String> context = new ThreadLocal<>();

    public void process(String val) {
        context.set(val);
        try {
            doWork();
        } catch (Exception e) {
        }
    }

    private void doWork() {
    }
}