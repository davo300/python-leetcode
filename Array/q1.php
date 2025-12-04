class Solution {

/**
 * @param Integer[] $nums
 * @param Integer $target
 * @return Integer[]
 */
function twoSum($nums, $target) {
    $map = [];  // value → index

    foreach ($nums as $i => $num) {
        $complement = $target - $num;

        if (array_key_exists($complement, $map)) {
            return [$map[$complement], $i];
        }

        $map[$num] = $i;
    }

    return [];  // no solution found
}
}