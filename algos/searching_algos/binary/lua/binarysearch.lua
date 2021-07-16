-- Search an table for a specified target using
-- the binary search algorithm
-- @param table table: The table to search
-- @param table_len number: The length of the table
-- @param target number: The item to find in the table
-- @return number: The index where the target was found
-- or -1 if the target was not found
local Table = {}

function Table.binarysearch(table, table_len, target)
        local left = 0
        local right = table_len - 1

        while left <= right do
                local middle = math.floor((left + right) / 2)

                if table[middle] < target then
                        left = middle + 1
                elseif table[middle] > target then
                        right = middle - 1
                else
                        return middle
                end
        end
        return -1
end

return Table
