package main.com.java.example;

import java.util.HashMap;
import java.util.Map;

public class CacheExample {

    private static Map<String, String> cache = new HashMap<>();

    public String getValue(String key) {
        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        String val = expensiveComputation(key);
        cache.put(key, val);
        return val;
    }

    private String expensiveComputation(String key) {
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
        }
        return "value-for-" + key;
    }
}