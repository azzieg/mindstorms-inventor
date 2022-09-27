from util.scratch import to_boolean

needle = "vent"
haystack = "inventor"
# Note that the case of the letters is normalized and hence effectively ignored.
contains = haystack.lower().find(needle.lower()) >= 0
return to_boolean(contains)
