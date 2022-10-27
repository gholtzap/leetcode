# @param {String} s
# @param {String} t
# @param {Integer} b
# @param {Boolean} output
# @return {Boolean}

# made in Ruby since strings are directly mutable

# language: ruby
# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 277 ms - top 50%
# Memory Usage: 216 MB - top 40%

def is_anagram(s, t)
    output = true
    if s.length != t.length
        output = false
    else 
        chars = t.split('')
    chars.each { |c|
        if s.include?(c)
            b = s.index(c) 
            s[b] = ' ';
        else 
            output = false
        end     
    } 
        return output
    end
end
    