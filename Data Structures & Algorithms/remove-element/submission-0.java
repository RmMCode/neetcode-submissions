class Solution {
    public int removeElement(int[] nums, int val) {
        int notVals = 0; // Where next valid element should be placed
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[notVals] = nums[i];
                notVals++;
            }
        }
        return notVals; // Number of elements not equal to val
    }
}