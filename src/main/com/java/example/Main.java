package main.com.java.example;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        UserService us = new UserService();
        us.createUsers(Arrays.asList("alice", "bob", "charlie"));

        WorkerPool wp = new WorkerPool();
        wp.startWorkers();

        CacheExample cache = new CacheExample();
        System.out.println(cache.getValue("k1"));

        ThreadLocalExample tle = new ThreadLocalExample();
        tle.process("ctx");
    }
}
