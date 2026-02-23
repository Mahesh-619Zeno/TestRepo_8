package main.com.java.example;

public class LockManager {

    private final Object lockA = new Object();
    private final Object lockB = new Object();

    public void first() {
        synchronized (lockB) {
            synchronized (lockA) {
                perform();
            }
        }
    }

    public void second() {
        synchronized (lockA) {
            synchronized (lockB) {
                perform();
            }
        }
    }

    private void perform() {
    }
}