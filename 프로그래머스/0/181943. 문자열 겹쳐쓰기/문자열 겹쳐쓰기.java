class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String x = my_string.substring(0, s);
        
        int len = s + overwrite_string.length();
        if (overwrite_string.length() >= my_string.length()-s) {
            answer = x + overwrite_string;
        } else {
            answer = x + overwrite_string + my_string.substring(len);
        }
            
        return answer;
    }
}