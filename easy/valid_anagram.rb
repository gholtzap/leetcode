@param {String} s
@param {String} t
@param {Integer} b
@param {Boolean} output
@return {Boolean}

# made in Ruby since strings are directly mutable
def is_anagram(s, t)
    output = true
    # anagrams have to be the same length, or else return false
    if s.length != t.length
        output = false
    # split second str into chars, then iterate over each char
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
    