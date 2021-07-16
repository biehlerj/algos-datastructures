local t = require("binarysearch")
-- test: target not found
T = {2, 3, 4, 10, 40}
local v = t.binarysearch(T, #T, 6); assert(v == -1)

-- test: target found
local v = t.binarysearch(T, #T, 10); assert(v == 4)
