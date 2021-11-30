from passport_module import Passport

class passport_parser:
    input = ['eyr:2033\n', 'hgt:177cm pid:173cm\n', 'ecl:utc byr:2029 hcl:#efcc98 iyr:2023\n', '\n',
             'pid:337605855 cid:249 byr:1952 hgt:155cm\n', 'ecl:grn iyr:2017 eyr:2026 hcl:#866857\n', '\n',
             'cid:242 iyr:2011 pid:953198122 eyr:2029 ecl:blu hcl:#888785\n', '\n', 'hgt:173cm hcl:#341e13\n',
             'cid:341\n', 'pid:112086592\n', 'iyr:2012 byr:2011 ecl:amb\n', 'eyr:2030\n', '\n', 'pid:790332032\n',
             'iyr:2019\n', 'eyr:2023 byr:1969 ecl:brn\n', 'hgt:163cm\n', 'hcl:#623a2f\n', '\n',
             'byr:1920 eyr:2023 cid:146 pid:890112986 hgt:171cm hcl:#b6652a iyr:2017 ecl:hzl\n', '\n',
             'hcl:#c0946f byr:1967 cid:199 ecl:gry\n', 'iyr:2012 pid:987409259 hgt:157cm eyr:2021\n', '\n',
             'pid:316587303 iyr:2016 eyr:2023 ecl:blu byr:1959 hgt:186cm hcl:#733820\n', '\n',
             'hcl:#fffffd hgt:152cm byr:1996 ecl:gry eyr:2024\n', '\n', 'ecl:brn hgt:185cm\n',
             'pid:648491325 byr:1967\n', 'hcl:#172f67 iyr:2014\n', 'eyr:2028\n', '\n',
             'pid:328737320 iyr:2017 hcl:#fffffd hgt:178\n', 'ecl:#35fad5\n', 'byr:1959\n', '\n',
             'iyr:2010 byr:1943 eyr:2028\n', 'hgt:178cm hcl:#888785 pid:572750267\n', '\n',
             'cid:175 ecl:brn eyr:2026 iyr:2017\n', 'hcl:#5d69b9 byr:1998 pid:289515215\n', 'hgt:151cm\n', '\n',
             'hgt:182cm\n', 'ecl:blu eyr:2028 iyr:2011 hcl:#a97842 pid:758494126\n', '\n', 'iyr:2023\n',
             'hgt:174cm hcl:cafc2f\n', 'ecl:utc\n', 'cid:299 eyr:2026 pid:57963956\n', '\n',
             'pid:853993893 ecl:blu hgt:188cm cid:294 hcl:#341e13 byr:1975\n', 'eyr:2027 iyr:2015\n', '\n',
             'ecl:amb hgt:70 iyr:2018 pid:241872490\n', 'byr:1962\n', 'eyr:2024 hcl:c5f0c3\n', '\n',
             'pid:994754974 eyr:2029 iyr:2017\n', 'cid:137 byr:1966 hcl:#733820 ecl:blu\n', '\n', 'ecl:utc\n',
             'pid:937481632 hgt:190\n', 'eyr:2025 iyr:2027 byr:1949 cid:84 hcl:d3f4f5\n', '\n',
             'cid:129 ecl:brn hgt:91 eyr:1932\n', 'iyr:2020 pid:298540404 hcl:#888785 byr:1986\n', '\n',
             'pid:416051368 eyr:2020 iyr:2011\n', 'hgt:93 byr:2023 hcl:#efcc98\n', 'ecl:amb\n', '\n',
             'byr:2010 hgt:181cm\n', 'iyr:2020\n', 'eyr:2040 pid:785862801 ecl:#f84ccd\n', '\n',
             'hgt:152cm iyr:2013 pid:932020343 eyr:2023 ecl:hzl byr:1920\n', 'hcl:#fffffd\n', '\n', 'hgt:152cm\n',
             'iyr:2020 byr:1993 hcl:#18171d pid:120354938\n', 'eyr:2021 ecl:gry\n', '\n', 'eyr:2025 byr:1996\n',
             'hcl:#623a2f\n', 'iyr:2018 ecl:oth cid:177 pid:904738945 hgt:164cm\n', '\n', 'pid:45042993\n',
             'hgt:193 iyr:2018 byr:2026 eyr:2026\n', 'hcl:#623a2f cid:175 ecl:brn\n', '\n',
             'byr:1956 ecl:hzl iyr:2020 pid:892810672 hgt:164cm eyr:2021 cid:186 hcl:#efcc98\n', '\n',
             'cid:314 hgt:180cm\n', 'ecl:amb hcl:#602927 byr:2027\n', 'iyr:1958\n', 'eyr:2020 pid:#b2b732\n', '\n',
             'cid:50\n', 'hcl:#a97842\n', 'hgt:155cm pid:667716485 ecl:gry iyr:2014 byr:1995 eyr:2029\n', '\n',
             'eyr:2030\n', 'pid:783631610\n', 'hgt:74\n', 'byr:2014 hcl:z iyr:2003 ecl:grt\n', '\n',
             'ecl:#d4d852 iyr:2029 hcl:z hgt:185in\n', 'eyr:2034 pid:#526166\n', '\n',
             'iyr:1946 eyr:1957 byr:1941 pid:632690435 ecl:oth hcl:18a37c hgt:59cm\n', '\n', 'iyr:2013\n',
             'eyr:2026 pid:002380966 cid:95\n', 'hcl:#623a2f byr:1965 ecl:oth\n', '\n',
             'ecl:gry pid:479214778 hcl:#18171d\n', 'byr:1928 cid:98 eyr:2020 iyr:2019 hgt:163cm\n', '\n',
             'hcl:#bd0f54 cid:225 eyr:2024 hgt:153cm iyr:2020\n', 'byr:1956 pid:048565668 ecl:hzl\n', '\n',
             'ecl:#5d8b3b hgt:156cm eyr:2029 pid:#3df0cc byr:1967 cid:118 hcl:e23f0f\n', '\n', 'pid:437721309\n',
             'hcl:#cfa07d hgt:181cm iyr:2019 cid:224 eyr:2028 byr:1946\n', 'ecl:gry\n', '\n', 'byr:1962\n',
             'eyr:2023\n', 'hgt:182cm\n', 'pid:733248003 ecl:blu\n', 'iyr:2014 hcl:#efcc98\n', '\n',
             'byr:1966 hgt:158cm\n', 'eyr:2029 hcl:#602927 iyr:2013\n', 'pid:963663665\n', '\n',
             'pid:529595074 byr:1940 eyr:2020 hcl:#c0946f cid:113 iyr:2015 ecl:oth\n', 'hgt:191cm\n', '\n', 'ecl:hzl\n',
             'hcl:#a97842\n', 'hgt:157cm eyr:2025 iyr:2015 byr:1978 pid:579525362\n', '\n',
             'ecl:oth hcl:#18171d cid:76 iyr:2011 eyr:2021\n', 'byr:1953 hgt:173cm pid:976483712\n', '\n',
             'ecl:brn hcl:#fffffd cid:242 pid:588299934\n', 'hgt:69in byr:1947\n', 'iyr:2010 eyr:2030\n', '\n',
             'hcl:#fffffd ecl:gry cid:93\n', 'pid:731904973 byr:1939 eyr:2029 iyr:2016\n', '\n',
             'pid:96716037 iyr:1938 eyr:2032\n', 'hgt:192 ecl:gmt byr:2029 hcl:02edc5\n', '\n', 'byr:1958\n',
             'iyr:2011 eyr:2029 ecl:gry\n', 'pid:526931024\n', 'hcl:z\n', 'hgt:59cm\n', '\n', 'byr:1966 ecl:hzl\n',
             'pid:378066668 hcl:#c0946f\n', 'iyr:2017 eyr:2026 cid:142 hgt:184cm\n', '\n', 'pid:1134356373\n',
             'iyr:2019\n', 'ecl:grn\n', 'hcl:#ceb3a1 byr:1950\n', 'hgt:154in\n', '\n', 'hgt:157cm ecl:zzz byr:1976\n',
             'pid:5047305958\n', 'iyr:2013 hcl:#341e13\n', '\n', 'eyr:2024\n',
             'hcl:#a97842 hgt:179cm pid:543943316 cid:214 ecl:brn\n', 'byr:1999\n', 'iyr:2017\n', '\n',
             'byr:1983 eyr:2024 hgt:177cm\n', 'ecl:hzl\n', 'iyr:2013 pid:328883228 hcl:#ceb3a1\n', '\n',
             'cid:226 pid:262286178 iyr:2010 ecl:grn byr:1962 eyr:2025 hcl:#efcc98\n', 'hgt:60in\n', '\n',
             'iyr:2029 ecl:#559ffe hcl:z\n', 'cid:156\n', 'byr:2003\n', 'hgt:178\n', 'pid:93994500\n', '\n',
             'iyr:2026 hcl:#eda7f3 ecl:amb\n', 'byr:1921 eyr:2021 pid:153cm\n', '\n', 'byr:1988\n',
             'ecl:amb hgt:178cm hcl:#2aea45\n', 'pid:70722502 eyr:2027 iyr:2015\n', '\n',
             'pid:555636800 eyr:2020 hgt:182cm iyr:2019 byr:1948 cid:325\n', 'hcl:#733820\n', '\n', 'eyr:1973\n',
             'iyr:2024 hcl:z byr:2028 ecl:dne cid:169\n', 'pid:43596015 hgt:170in\n', '\n', 'hcl:#b6652a ecl:gry\n',
             'cid:264\n', 'hgt:178cm iyr:2027 pid:23042405 byr:1947 eyr:2024\n', '\n', 'byr:1989\n',
             'pid:266274644 ecl:blu eyr:2023 hcl:#733820\n', 'hgt:192cm iyr:2018 cid:272\n', '\n',
             'iyr:2013 hcl:z hgt:73cm byr:2014 pid:192cm ecl:#1627a7\n', '\n', 'pid:816749378 hgt:178cm\n',
             'hcl:#733820 eyr:2029\n', 'byr:1993\n', '\n',
             'hcl:0cacc5 byr:1944 iyr:2028 eyr:2024 hgt:163in pid:74169361\n', 'ecl:dne\n', '\n', 'hcl:#ceb3a1\n',
             'ecl:grn\n', 'eyr:2027 pid:481186415 hgt:176cm cid:325\n', 'byr:1986\n', '\n',
             'eyr:2028 hgt:174cm ecl:brn\n', 'hcl:#888785 iyr:2015 pid:064161451 byr:1969\n', '\n',
             'ecl:brn cid:323 hgt:167\n', 'byr:1993 iyr:1953\n', 'hcl:z eyr:2023 pid:161542750\n', '\n',
             'ecl:#895336 eyr:2033 hgt:67cm cid:254 iyr:1967 hcl:z byr:1954\n', '\n', 'ecl:#9dbea3 iyr:2018 eyr:2035\n',
             'hgt:183\n', 'pid:747501524 hcl:#fd8515 cid:110\n', 'byr:1997\n', '\n', 'ecl:utc\n',
             'iyr:2014 hgt:183in byr:2007 eyr:2026 hcl:#cfa07d\n', 'cid:334\n', '\n',
             'ecl:gry hcl:#b6652a pid:250420128\n', 'eyr:2024 byr:1939 hgt:170cm\n', '\n',
             'hcl:#18171d eyr:2030 byr:1925 pid:204206116\n', 'iyr:2014 hgt:174cm ecl:hzl\n', '\n',
             'iyr:2020 hcl:#efcc98\n', 'pid:393444692\n', 'ecl:oth hgt:152cm byr:1957 eyr:2021\n', '\n',
             'byr:1973 eyr:2024 iyr:2014 hcl:#602927\n', 'pid:832320186 hgt:166cm ecl:grn\n', '\n',
             'pid:192524664 hgt:182cm\n', 'hcl:#18171d\n', 'ecl:oth eyr:2030 byr:1942 iyr:2013\n', '\n',
             'hgt:129 byr:2016 hcl:6734a1 ecl:#915282 iyr:1949 cid:130 pid:677408864 eyr:2030\n', '\n',
             'eyr:2028 ecl:gry hgt:171cm byr:1960 iyr:2020 pid:688526729 cid:262 hcl:#733820\n', '\n',
             'ecl:grn iyr:2019 pid:775867641 hcl:#bf1e29\n', 'byr:1920 hgt:163cm\n', '\n', 'eyr:2029 hcl:#866857\n',
             'iyr:2024\n', 'pid:170cm byr:1931\n', 'hgt:177cm ecl:hzl cid:312\n', '\n',
             'iyr:2019 ecl:#19fef5 pid:2080468234\n', 'eyr:2008 hgt:72\n', 'hcl:e14dfe\n', 'byr:1980 cid:272\n', '\n',
             'byr:2025\n', 'cid:163\n', 'iyr:2020 pid:758946748 hgt:161cm\n', 'ecl:amb eyr:2023 hcl:026d4d\n', '\n',
             'iyr:2021 cid:109\n', 'eyr:2032 byr:2010\n', 'hcl:#fffffd pid:874586711 ecl:hzl hgt:142\n', '\n',
             'eyr:2023\n', 'hcl:z iyr:2019 byr:2013 ecl:#b42611 pid:164cm hgt:60cm\n', '\n',
             'byr:1935 cid:226 hcl:#602927 ecl:blu pid:700452129 eyr:2029\n', 'iyr:2016 hgt:180cm\n', '\n',
             'hgt:179cm\n', 'pid:181cm\n', 'ecl:gry cid:309\n', 'eyr:2029\n', 'hcl:#6b5442\n', 'byr:1987\n',
             'iyr:2010\n', '\n', 'ecl:gry byr:1986 hcl:#cce4b8\n', 'pid:101583943 iyr:2010 hgt:65cm eyr:2021\n', '\n',
             'cid:168\n', 'pid:#8556c9 hcl:413944 eyr:2036 byr:2013 iyr:2012\n', 'ecl:#66dc1c hgt:59cm\n', '\n',
             'eyr:1984 byr:2017 pid:#cbc84e hcl:z\n', 'cid:189 iyr:2021 ecl:blu\n', 'hgt:152cm\n', '\n',
             'byr:1993 hcl:#004c11 eyr:2026\n', 'iyr:2010\n', 'ecl:brn hgt:188cm\n', 'pid:889959941\n', '\n',
             'hgt:172 byr:2008 eyr:2030 iyr:1959\n', 'ecl:oth hcl:#a8ebbb\n', '\n',
             'iyr:2013 hcl:#8f97b1 hgt:182cm ecl:grn cid:89\n', 'eyr:2029\n', 'byr:1974\n', '\n',
             'eyr:2025 hcl:#6b5442 pid:222418968 byr:1951 cid:105 ecl:hzl iyr:2011 hgt:181cm\n', '\n', 'iyr:2017\n',
             'ecl:brn pid:481721303 hgt:190cm\n', 'eyr:2037 byr:1990 hcl:#ceb3a1\n', '\n', 'hcl:z\n', 'pid:85905429\n',
             'byr:1923 cid:260\n', 'eyr:2031 ecl:gry\n', 'iyr:2022 hgt:180cm\n', '\n', 'hcl:#fffffd hgt:76cm\n',
             'ecl:grn\n', 'pid:39254112 byr:2010 iyr:1961 eyr:2028\n', '\n', 'ecl:brn iyr:2016\n',
             'eyr:2027 hcl:#efcc98 pid:753268957 hgt:60in byr:1943\n', '\n', 'ecl:oth\n', 'pid:087762106 hgt:190cm\n',
             'byr:1974 cid:171 hcl:#c63f21\n', 'eyr:2020\n', '\n', 'ecl:#8c1b6c\n', 'byr:1962 iyr:2007 pid:106672731\n',
             'hgt:172in cid:239 eyr:2026 hcl:#b6652a\n', '\n', 'hgt:170cm eyr:2021\n',
             'cid:219 hcl:#a97842 pid:040224991 byr:1950 iyr:2018\n', '\n', 'byr:2029\n', 'eyr:2036 cid:309\n',
             'iyr:2016 hgt:167cm hcl:#fffffd\n', 'ecl:#1ab23b\n', '\n', 'iyr:2013 ecl:gry eyr:2020 pid:947828194\n',
             'hcl:#18171d hgt:163cm byr:1971\n', '\n', 'hcl:#fffffd iyr:2011\n', 'pid:150105713 eyr:2029\n',
             'hgt:168cm byr:1925 ecl:hzl\n', '\n', 'cid:253\n', 'hcl:#341e13\n', 'eyr:2025 hgt:184cm\n',
             'pid:651786830 byr:1936 iyr:2013\n', 'ecl:hzl\n', '\n', 'pid:7328393469\n',
             'hgt:175cm ecl:gry iyr:2012 byr:1963 hcl:#623a2f eyr:2026\n', '\n',
             'eyr:2029 pid:669044398 hgt:161cm hcl:#cfa07d ecl:gry iyr:2018\n', '\n',
             'pid:920006222 byr:1941 ecl:grn eyr:2027 cid:87 hcl:#733820\n', 'iyr:2018 hgt:171cm\n', '\n',
             'byr:1964 hgt:157cm hcl:#a97842\n', 'pid:756972774 eyr:2024 iyr:2013 ecl:gry\n', '\n',
             'iyr:2010 cid:279\n', 'hgt:189cm byr:1959\n', 'ecl:brn eyr:2022 pid:937686753 hcl:#602927\n', '\n',
             'iyr:2013\n', 'eyr:2027 cid:223 pid:145547438\n', 'hcl:#6e6f47 hgt:165cm ecl:amb\n', '\n', 'byr:2009\n',
             'ecl:oth hcl:#623a2f\n', 'hgt:166cm eyr:2034 pid:120339592\n', 'iyr:2012\n', '\n',
             'eyr:2026 hcl:z byr:2018 pid:7809314464 iyr:2012 hgt:158cm ecl:hzl\n', '\n', 'cid:291 hgt:168\n',
             'ecl:#7734de iyr:2021 hcl:5b4ef1 pid:3381158334 eyr:1956 byr:2003\n', '\n', 'iyr:2015 hcl:#cfa07d\n',
             'byr:1971 eyr:2023\n', 'ecl:oth pid:560419063 cid:155 hgt:170cm\n', '\n',
             'eyr:2021 hgt:189cm iyr:2014 hcl:#6b5442 ecl:brn cid:287\n', 'byr:1951 pid:936881112\n', '\n',
             'iyr:2013\n', 'eyr:2020 ecl:hzl hgt:150cm cid:210\n', 'pid:032458640 byr:1920 hcl:#6b5442\n', '\n',
             'hgt:180cm hcl:#cfa07d ecl:grn eyr:2027\n', 'pid:140859202 iyr:2014 cid:232\n', 'byr:1932\n', '\n',
             'pid:68300657 byr:1988 hgt:181cm\n', 'ecl:hzl iyr:1951 hcl:e18469\n', 'eyr:2013\n', '\n',
             'pid:157572693 hgt:185cm\n', 'hcl:#065fe8 ecl:gry eyr:2027\n', 'iyr:2014\n', '\n',
             'eyr:2029 hgt:164cm hcl:z ecl:grn cid:270 iyr:2019 byr:1993 pid:338068138\n', '\n',
             'iyr:2016 cid:131 byr:1990 hcl:#7d3b0c ecl:grn pid:066023454 hgt:154cm\n', 'eyr:2025\n', '\n',
             'iyr:2019 eyr:2024 hgt:174cm\n', 'pid:855792798 byr:1920 hcl:#cfa07d\n', '\n', 'eyr:2020\n',
             'hgt:74in iyr:2013 ecl:amb\n', 'byr:1920 hcl:3f6214\n', 'pid:957164804\n', '\n',
             'pid:756767000 hcl:#220540 byr:1922 hgt:172cm\n', 'eyr:2023 cid:305 ecl:hzl iyr:2019\n', '\n',
             'hgt:193in eyr:2025 pid:117240526 iyr:2017 hcl:#888785 byr:1928 ecl:blu\n', '\n', 'byr:1942\n',
             'ecl:blu\n', 'cid:347\n', 'hcl:#fffffd eyr:2023 iyr:2017\n', 'hgt:154cm pid:836554235\n', '\n',
             'eyr:2023 hcl:#efcc98\n', 'pid:364475403 byr:1962 iyr:2015\n', 'ecl:brn hgt:59in cid:289\n', '\n',
             'byr:2021 hcl:ca4bcf hgt:88 iyr:2017 ecl:gmt pid:181cm eyr:2032\n', '\n',
             'byr:1937 iyr:2014 hgt:154cm ecl:brn\n', 'hcl:#866857\n', 'eyr:2022 pid:234591437\n', '\n',
             'iyr:2002 cid:139 byr:1982\n', 'hcl:#c0946f\n', 'pid:#62721b hgt:159in eyr:1966 ecl:brn\n', '\n',
             'eyr:2036 ecl:oth byr:2026 hgt:96\n', 'pid:137651094\n', 'hcl:z\n', '\n', 'pid:373485985\n',
             'iyr:2030 ecl:gry byr:2011 hgt:65cm\n', 'hcl:#733820\n', '\n', 'pid:390979357\n', 'ecl:gry hgt:164cm\n',
             'hcl:#ceb3a1 eyr:2029 byr:1932 iyr:2015\n', '\n',
             'ecl:hzl hgt:68in eyr:2023 pid:829734763 iyr:2016 hcl:#733820 byr:1997\n', '\n',
             'hgt:150cm byr:1926 iyr:2019 pid:521908229 eyr:2029 ecl:brn hcl:#623a2f\n', '\n', 'eyr:2023 byr:1974\n',
             'iyr:2018 cid:58\n', 'ecl:grn\n', 'pid:310883188 hcl:#866857\n', 'hgt:164cm\n', '\n',
             'byr:1963 iyr:2019\n', 'hgt:162cm\n', 'eyr:2021\n', 'hcl:#fffffd ecl:oth pid:104734523\n', '\n',
             'hcl:#888785 cid:150\n', 'eyr:2020 byr:1988\n', 'iyr:2018\n', 'ecl:oth\n', 'hgt:179cm pid:635972018\n',
             '\n', 'iyr:2014 hcl:#7d3b0c ecl:hzl pid:717760687\n', 'byr:1929 eyr:2027 hgt:183cm\n', '\n',
             'iyr:2019 byr:2000\n', 'eyr:2025 pid:506581828 hcl:#602927 ecl:oth\n', 'hgt:162cm\n', '\n',
             'pid:#fd3377 ecl:#618bce hcl:#ceb3a1\n', 'iyr:1944 hgt:182cm cid:57\n', 'byr:2022 eyr:1995\n', '\n',
             'pid:4790730010\n', 'hgt:192cm\n', 'cid:222 byr:2022\n', 'hcl:4798e7 ecl:#5126d5 iyr:1954 eyr:2040\n',
             '\n', 'hcl:#b6652a\n', 'ecl:brn cid:181 pid:983890186 hgt:189cm byr:1998\n', 'eyr:2022 iyr:2011\n', '\n',
             'iyr:2018 eyr:2022\n', 'cid:58 byr:1994 hgt:169cm ecl:hzl pid:036522894\n', 'hcl:#2c9ee8\n', '\n',
             'iyr:1979\n', 'hcl:e09b9c byr:2016\n', 'hgt:121 eyr:1962 pid:#fb14be cid:265 ecl:lzr\n', '\n',
             'eyr:2024 hgt:63in hcl:#efcc98 iyr:2018\n', 'byr:1953 pid:881102827 ecl:amb\n', '\n',
             'ecl:oth hgt:177cm eyr:2028 iyr:2011\n', 'hcl:#efcc98 pid:113579849 byr:1957\n', '\n',
             'ecl:#fe1b74 iyr:1926 hgt:70cm\n', 'pid:70807766 hcl:556dca byr:2030\n', 'eyr:2032\n', '\n',
             'byr:1997 ecl:blu hgt:105\n', 'pid:178655906 iyr:2025\n', 'hcl:#6b5442\n', 'eyr:2021\n', '\n',
             'eyr:2030 ecl:grt hgt:161cm hcl:#ceb3a1 iyr:2016\n', 'pid:318930966 cid:59 byr:1924\n', '\n',
             'cid:200 hgt:67in\n', 'pid:229395752 byr:1936 ecl:oth iyr:2013 eyr:2020 hcl:#c0946f\n', '\n',
             'byr:1990 iyr:2018\n', 'cid:99 hcl:#6b5442 hgt:155 pid:350832537 ecl:blu eyr:2021\n', '\n',
             'eyr:2039 byr:2025 pid:247367429 hcl:z iyr:2013 ecl:amb\n', 'cid:118\n', '\n', 'eyr:2027 hcl:z ecl:utc\n',
             'cid:274 hgt:175in iyr:2016 byr:1977 pid:478855994\n', '\n', 'eyr:2020 pid:636743032\n',
             'hcl:#64a8b8 iyr:2018 ecl:grn hgt:68in byr:1969\n', '\n',
             'pid:515635081 iyr:2013 byr:1980 eyr:2024 hgt:173cm ecl:gry\n', 'hcl:#b6652a\n', '\n',
             'ecl:utc byr:2026 iyr:1999 eyr:1937\n', 'hgt:66cm\n', 'hcl:z\n', 'pid:2247643960\n', '\n',
             'iyr:2013 byr:1942 hgt:154cm eyr:2020 hcl:#18171d cid:323 pid:302753381 ecl:oth\n', '\n',
             'ecl:xry pid:346719476\n', 'iyr:1999\n', 'eyr:2020 hgt:154cm hcl:z\n', 'byr:2027\n', '\n',
             'hgt:160cm eyr:2025 hcl:#fffffd byr:1998\n', 'pid:678119271 ecl:blu iyr:2014\n', '\n',
             'hgt:161cm iyr:2011\n', 'ecl:blu\n', 'byr:1921 pid:236833613 eyr:2021\n', 'hcl:#623a2f\n', '\n',
             'ecl:hzl hcl:#18171d hgt:151cm pid:541887993\n', 'byr:1995 iyr:2019 eyr:2021\n', '\n',
             'pid:496474711 byr:1966 ecl:gry eyr:2025 hgt:176cm\n', 'hcl:#b6652a iyr:2018\n', '\n',
             'iyr:2010 hcl:#efcc98 pid:351846405\n', 'eyr:2024 hgt:150cm\n', 'byr:1941\n', '\n',
             'hgt:151cm ecl:gry hcl:#a97842 pid:586789406\n', 'eyr:2022 iyr:2013 byr:1982\n', '\n',
             'byr:1994 eyr:2028 ecl:gry\n', 'hcl:#888785 iyr:2010\n', 'hgt:165cm cid:183\n', '\n', 'iyr:2015\n',
             'byr:1933 hcl:#733820 hgt:167cm\n', 'ecl:blu pid:914665208 eyr:2027\n', '\n', 'eyr:2031 hcl:6804ef\n',
             'ecl:amb\n', 'byr:2024\n', 'hgt:157cm iyr:1938\n', 'pid:#0418fb\n', '\n', 'byr:1936\n',
             'ecl:oth hgt:190cm cid:91\n', 'pid:711544430 iyr:2020\n', 'eyr:2025 hcl:#888785\n', '\n',
             'pid:381452527\n', 'eyr:2027 hcl:#efcc98 ecl:brn\n', 'byr:1956 hgt:63in\n', '\n', 'ecl:oth\n',
             'iyr:2014 hcl:#ceb3a1\n', 'cid:254\n', 'pid:544612871 byr:1985 eyr:2023 hgt:172cm\n', '\n',
             'hcl:#efcc98\n', 'hgt:191cm byr:1948\n', 'ecl:blu eyr:2028\n', 'pid:953894279 iyr:2017\n', '\n',
             'byr:1968 pid:875469219\n', 'hcl:#efcc98 hgt:176cm cid:141 iyr:2017\n', '\n',
             'eyr:2022 hcl:#733820 ecl:hzl\n', 'pid:870733357 iyr:2013\n', 'byr:1949 hgt:150cm cid:252\n', '\n',
             'ecl:gry\n', 'hcl:#602927 pid:632246684 byr:1986\n', 'eyr:2030 hgt:152cm iyr:2013\n', '\n', 'eyr:2029\n',
             'iyr:2016\n', 'byr:1969 pid:595125675 ecl:gry hcl:#cfa07d hgt:184cm\n', '\n', 'byr:1947 hcl:z\n',
             'cid:188 eyr:2038 pid:177cm iyr:2011 hgt:166cm ecl:#c1376b\n', '\n',
             'ecl:hzl hgt:170cm cid:307 eyr:2022\n', 'byr:1971\n', 'hcl:#b6652a pid:047040501\n', '\n',
             'hgt:126 ecl:zzz\n', 'byr:2019\n', 'pid:170207910 eyr:2035 hcl:23df48\n', 'iyr:1932\n', '\n',
             'hgt:152cm cid:270 eyr:2036 ecl:#408f6e iyr:1952 pid:5808880830 byr:2022\n', 'hcl:0b1ba6\n', '\n',
             'eyr:2021 hgt:179cm\n', 'byr:1938 pid:140937061 iyr:2030 hcl:#a97842 ecl:oth\n', '\n',
             'hgt:67cm eyr:2028 pid:816355657\n', 'iyr:2019 byr:2008 hcl:z ecl:#5b4f31\n', '\n', 'cid:192\n',
             'iyr:2018 eyr:2020 byr:1983 pid:873720366\n', 'ecl:grn hgt:187cm hcl:#6b5442\n', '\n',
             'byr:1955 hgt:71in iyr:2018 pid:320019385 hcl:#6b5442\n', 'cid:324 eyr:2027\n', '\n', 'pid:957860464\n',
             'hcl:#602927\n', 'iyr:2011\n', 'byr:2026 cid:261 eyr:2006\n', '\n',
             'byr:1989 ecl:gry cid:143 pid:258434299 eyr:2027 hgt:192cm iyr:2017 hcl:#7d3b0c\n', '\n', 'pid:#1742ae\n',
             'ecl:#a61090\n', 'iyr:2028 hcl:717dd0 hgt:139 cid:183\n', 'eyr:2035\n', '\n',
             'eyr:2028 pid:039325804 hgt:167cm hcl:#888785 ecl:oth cid:155 iyr:2013 byr:1923\n', '\n',
             'byr:1956 iyr:2010\n', 'hcl:#d683bf\n', 'eyr:2023\n', 'hgt:70in\n', 'cid:197 pid:143320690\n', 'ecl:hzl\n',
             '\n', 'ecl:#4004e3 cid:278\n', 'iyr:1950 pid:745107377\n', 'byr:2007 eyr:2036\n', 'hcl:8447eb hgt:74cm\n',
             '\n', 'hcl:#ceb3a1 hgt:177cm iyr:2010 pid:640032134\n', 'ecl:gry\n', 'eyr:2027 byr:1958\n', '\n',
             'hgt:187cm\n', 'iyr:1921 ecl:#1c7d96\n', 'eyr:1987\n', 'byr:2028 pid:#28e5a1 cid:144 hcl:9fc25d\n', '\n',
             'iyr:2012 byr:1996 cid:289 hgt:177cm hcl:#fffffd pid:687240168 eyr:2030 ecl:gry\n', '\n',
             'pid:860410143 ecl:dne eyr:2031 cid:206 hgt:187in byr:1927\n', 'hcl:8c2149 iyr:2012\n', '\n', 'iyr:2010\n',
             'byr:1963 cid:139 pid:160019759\n', 'eyr:2030 hgt:172cm hcl:#602927\n', '\n', 'pid:309851270\n',
             'iyr:2014\n', 'ecl:hzl byr:1939\n', 'cid:71\n', 'eyr:2030\n', 'hcl:#b216fb\n', 'hgt:161cm\n', '\n',
             'ecl:gry\n', 'cid:138\n', 'iyr:2014\n', 'hgt:177cm byr:1942\n', 'pid:900269082 eyr:2024 hcl:#fffffd\n',
             '\n', 'iyr:2019 hgt:158cm\n', 'hcl:#18171d pid:941939350 eyr:2024 ecl:brn byr:1944\n', '\n',
             'byr:2023 ecl:brn\n', 'cid:101 eyr:2016 pid:190078757 hgt:188in\n', '\n', 'cid:188\n',
             'ecl:blu pid:075499609\n', 'byr:1970\n', 'hcl:#fffffd hgt:164cm eyr:2028 iyr:2015\n', '\n',
             'byr:2011 hcl:z\n', 'ecl:gry\n', 'pid:408316491 hgt:64cm iyr:2017 eyr:1968\n', '\n',
             'ecl:oth hcl:#6b5442\n', 'pid:623099801\n', 'hgt:163cm\n', 'byr:1928\n', '\n', 'pid:165230004\n',
             'ecl:grn byr:1935 hcl:#c0946f iyr:2012\n', 'hgt:185cm\n', '\n',
             'hgt:162cm pid:069876432 byr:1960 cid:326 iyr:2013\n', 'hcl:#cfa07d eyr:2021\n', 'ecl:grn\n', '\n',
             'ecl:#f3d8ba hgt:182cm eyr:2020 byr:2007\n', 'hcl:z iyr:2014 pid:6141297559\n', '\n', 'pid:867747198\n',
             'hcl:#efcc98\n', 'eyr:2030 byr:1989\n', 'hgt:181cm\n', '\n', 'byr:2000 eyr:2021 hgt:166cm\n',
             'hcl:#fffffd iyr:2019 pid:546346187 cid:111 ecl:grn\n', '\n', 'eyr:2034 hcl:#623a2f\n', 'byr:1958\n',
             'pid:60553207 ecl:#76b538 hgt:59 cid:75\n', '\n', 'hcl:#623a2f\n', 'eyr:2023 pid:251940892 byr:1998\n',
             'iyr:2012\n', 'hgt:181cm ecl:gry\n', '\n', 'iyr:2020 cid:83\n',
             'byr:1938 eyr:2024 ecl:amb pid:046668488 hgt:181cm hcl:#341e13\n', '\n', 'ecl:grn\n',
             'eyr:2036 iyr:1951 byr:2029 hcl:z hgt:177in\n', 'pid:135470038\n', '\n', 'iyr:2015 eyr:2023\n',
             'byr:1961\n', 'cid:81 hcl:#a97842 pid:710065884\n', 'hgt:152cm\n', 'ecl:#1f9801\n', '\n', 'byr:2014\n',
             'pid:25253929 hcl:z\n', 'ecl:#f3fb41 eyr:2025 cid:255 iyr:1998\n', 'hgt:155cm\n', '\n',
             'ecl:gry pid:919070381 hcl:#efcc98 iyr:2019 eyr:2021 byr:1995\n', '\n', 'byr:1942\n', 'eyr:2029\n',
             'hgt:191cm hcl:#18171d\n', 'pid:649719423 iyr:2018 ecl:brn\n', '\n', 'ecl:gry\n',
             'byr:1963 iyr:2016 hgt:188cm pid:024539026 eyr:2022\n', '\n', 'hgt:176cm\n',
             'ecl:hzl eyr:1923 pid:176188310 hcl:#b6652a\n', 'byr:1939\n', 'iyr:2011\n', '\n',
             'iyr:2011 hcl:#888785 eyr:2030 ecl:gry byr:1920\n', '\n', 'pid:#0468a7 hcl:851fe0 eyr:2036 hgt:60cm\n',
             'byr:2030\n', 'iyr:1995\n', 'ecl:utc\n', '\n', 'hcl:#866857 iyr:2016 ecl:oth\n',
             'pid:414233531 eyr:2022 byr:1957\n', 'hgt:169cm cid:229\n', '\n', 'cid:185 ecl:#5f6f53\n',
             'pid:#20f317 byr:2024 eyr:1988 hcl:z iyr:2023 hgt:158in\n', '\n',
             'pid:015894427 eyr:2027 hgt:177cm ecl:blu\n', 'cid:222\n', 'hcl:#c0946f iyr:2010 byr:1993\n', '\n',
             'cid:101 hgt:162cm hcl:#c0946f pid:666662343 ecl:grn\n', 'byr:1974\n', 'iyr:2019\n', 'eyr:2029\n', '\n',
             'pid:782547454 hcl:z ecl:#b0805f\n', 'iyr:2013 eyr:2023\n', 'hgt:159cm\n', 'byr:1935\n', 'cid:230\n', '\n',
             'pid:298008321 hcl:231e1b hgt:166cm ecl:oth\n', 'iyr:2026 eyr:2020\n', '\n',
             'pid:230201309 iyr:2010 eyr:2025 hcl:#6b5442\n', 'cid:238\n', 'ecl:grn\n', 'hgt:174cm\n', '\n',
             'cid:287 eyr:2026 hcl:#733820\n', 'pid:201750712 iyr:2010\n', 'ecl:oth byr:1985\n', 'hgt:185cm\n', '\n',
             'hcl:#a97842 hgt:70in eyr:2029\n', 'pid:419407059 ecl:grn byr:1987\n', 'iyr:2016\n', '\n',
             'hgt:191cm byr:1951\n', 'eyr:2027 hcl:#8a9477 iyr:2015 ecl:amb pid:769071985\n', '\n', 'hcl:#6b5442\n',
             'iyr:2012 ecl:blu\n', 'cid:336 pid:391608810 byr:1995\n', 'eyr:2022\n', 'hgt:161cm\n', '\n', 'iyr:2020\n',
             'byr:1938\n', 'pid:927067439 eyr:2027 hgt:173cm\n', 'hcl:306963 ecl:xry\n', '\n', 'byr:1991\n',
             'iyr:2021 hgt:175cm hcl:68b4f3 ecl:utc\n', 'pid:037777327 eyr:2026\n', '\n', 'hgt:64in\n',
             'eyr:2025 hcl:#da6977 cid:137 byr:1990 iyr:2013 pid:918997697 ecl:amb\n', '\n',
             'iyr:2011 ecl:gry hgt:173cm eyr:2023 pid:802831612\n', 'hcl:#733820 byr:1976\n', '\n',
             'byr:1938 eyr:2021 pid:575395401 cid:234\n', 'hcl:#866857 ecl:hzl hgt:176cm\n', '\n',
             'hcl:#ceb3a1 ecl:hzl\n', 'eyr:2035\n', 'iyr:2014\n', 'byr:2019\n', '\n', 'ecl:hzl pid:961361236\n',
             'hgt:193cm hcl:#efcc98\n', 'iyr:2011 eyr:2030 byr:1967\n', '\n', 'eyr:1936 ecl:blu\n',
             'hgt:153cm hcl:98d3f0 pid:7296832671\n', 'byr:1931 iyr:1962\n', '\n',
             'iyr:2016 eyr:2024 hcl:#6b5442 ecl:grn\n', 'pid:265815316 byr:1966\n', 'hgt:165cm\n', '\n',
             'pid:203025149\n', 'eyr:2029\n', 'iyr:2010 cid:124 byr:1999 ecl:blu\n', '\n',
             'iyr:2011 eyr:2028 pid:#7e0612 byr:1924 hcl:#7d3b0c ecl:oth\n', 'hgt:82\n', '\n', 'ecl:hzl\n',
             'byr:1941\n', 'hcl:#b6652a eyr:2020 pid:409573276\n', 'iyr:1976 hgt:166cm\n', '\n', 'ecl:grn eyr:2030\n',
             'hgt:163cm iyr:2011 pid:121609314 byr:1961 hcl:#426e1a\n', '\n', 'pid:#49ea2c\n',
             'eyr:2029 hcl:#6b5442 iyr:1931\n', 'hgt:62cm ecl:brn\n', 'byr:2012\n', '\n',
             'eyr:2038 hcl:8d1f49 ecl:#6d4ea1 pid:0853660207 byr:2020 hgt:71cm\n', '\n', 'ecl:hzl hgt:170cm\n',
             'iyr:2011\n', 'byr:1966 eyr:2028\n', 'pid:609548717 hcl:#c0946f\n', '\n',
             'byr:1921 hcl:#c0946f ecl:blu iyr:2019 eyr:2024 pid:643387204\n', '\n', 'cid:324 hgt:162cm ecl:amb\n',
             'hcl:#18171d byr:1961\n', 'eyr:2027 iyr:2010 pid:939720354\n', '\n', 'byr:1933 hcl:#fffffd\n',
             'pid:353343882\n', 'eyr:2025 hgt:171cm ecl:amb cid:329\n', 'iyr:2017\n', '\n', 'byr:2004 iyr:2022\n',
             'pid:157cm eyr:2035\n', 'ecl:#eafe47 hgt:129\n', 'hcl:z\n', '\n',
             'cid:55 iyr:2025 hgt:177in pid:493884348\n', 'hcl:#888785 byr:1925 ecl:#b11d27 eyr:2036\n', '\n',
             'ecl:hzl\n', 'hgt:171cm\n', 'iyr:2012 pid:479669573 cid:335 hcl:#fffffd byr:1953\n', 'eyr:2029\n', '\n',
             'byr:1930 hcl:5bdf31\n', 'pid:#b21f8a hgt:164cm\n', 'cid:134\n', 'iyr:2023 ecl:lzr\n', '\n',
             'iyr:2018 eyr:2026 ecl:grn\n', 'pid:541667478 hcl:#6b5442 byr:1992 hgt:155cm\n', '\n',
             'hcl:2a1c4f iyr:2011\n', 'hgt:192cm eyr:2028 byr:2029 cid:270 ecl:dne pid:7995627426\n', '\n',
             'byr:1929 ecl:oth\n', 'pid:954905104 iyr:2016\n', 'hgt:68in hcl:#7d3b0c eyr:2020\n', '\n',
             'cid:167 byr:2000 hgt:186cm iyr:2013 hcl:#ff4019 pid:384287209\n', 'eyr:2024 ecl:amb\n', '\n',
             'eyr:2022\n', 'iyr:2018 byr:1972 cid:290\n', 'hgt:170cm ecl:grn pid:127269636\n', '\n', 'byr:1997\n',
             'ecl:amb hgt:150cm\n', 'pid:056368047 hcl:#fffffd eyr:2020 iyr:2020\n', '\n',
             'ecl:gry hgt:167in byr:2020 cid:131 pid:651833067 hcl:#623a2f iyr:2027 eyr:2038\n', '\n', 'hcl:#56c370\n',
             'iyr:2014\n', 'byr:1941\n', 'pid:654258425 hgt:184cm\n', 'eyr:2025 ecl:hzl\n', '\n', 'pid:571765355\n',
             'byr:2021\n', 'hcl:z\n', 'eyr:1921 cid:106 iyr:1978\n', 'ecl:#1162c5\n', 'hgt:184in\n', '\n',
             'iyr:2015 hcl:#18171d cid:237 pid:348578306 ecl:blu\n', 'byr:1988 eyr:2025 hgt:155cm\n', '\n',
             'byr:1963 hcl:#733820 cid:145 eyr:2030 ecl:oth pid:964094037 hgt:164cm iyr:2018\n', '\n',
             'pid:595618708 ecl:amb\n', 'hcl:#866857\n', 'hgt:186cm eyr:2024 byr:1924 iyr:2014\n', '\n',
             'ecl:hzl pid:484466493\n', 'hgt:176cm iyr:2016 byr:1983 hcl:#ceb3a1\n', '\n', 'ecl:gry hcl:#6b5442\n',
             'hgt:185cm\n', 'eyr:2029\n', 'pid:045583320 byr:1974 iyr:2020\n', '\n', 'ecl:brn hcl:352cf1 cid:149\n',
             'hgt:184cm byr:2011\n', 'eyr:2031\n', 'pid:21942403 iyr:2028\n', '\n',
             'ecl:brn eyr:2029 pid:083295950 byr:1995 hgt:176cm hcl:#c0946f\n', 'cid:68 iyr:2014\n', '\n',
             'hgt:170cm\n', 'byr:1945 hcl:#623a2f\n', 'iyr:2013 pid:912213595 ecl:gry eyr:2020\n', '\n', 'ecl:gry\n',
             'hcl:#18171d iyr:2015 hgt:185cm eyr:2023\n', 'byr:1950\n', '\n',
             'byr:1997 hgt:68in pid:368643584 hcl:#623a2f ecl:hzl eyr:2029 iyr:2012\n', 'cid:239\n', '\n',
             'iyr:2003 eyr:2020 cid:99 byr:2027 hcl:2c10a6 hgt:74cm\n', 'ecl:brn\n', '\n',
             'pid:151cm hcl:46a5fd eyr:2031\n', 'iyr:2014\n', 'byr:2005 ecl:xry hgt:176cm\n', '\n',
             'byr:2011 ecl:oth pid:821123244\n', 'iyr:2022\n', 'hcl:839b47 eyr:2039 hgt:150in\n', '\n',
             'pid:604669618 hgt:152cm iyr:2013\n', 'byr:1954\n', 'eyr:2021 ecl:amb hcl:#623a2f\n', '\n', 'hgt:182cm\n',
             'byr:1993\n', 'cid:177 hcl:#b6652a ecl:gry iyr:2011 pid:441649857 eyr:2027\n', '\n', 'cid:296 hgt:98\n',
             'ecl:grt iyr:2028 hcl:#a97842 byr:2022\n', 'pid:69736889 eyr:1935\n', '\n', 'iyr:2016 hcl:#cfa07d\n',
             'byr:1941\n', 'hgt:182cm\n', 'pid:720595987 ecl:gry\n', 'eyr:2022\n', '\n',
             'iyr:2018 hgt:164cm hcl:#650d28 byr:1973 cid:108 pid:#b0df80 ecl:blu eyr:2020\n', '\n', 'hcl:z\n',
             'pid:315901778\n', 'iyr:2013\n', 'byr:1999 ecl:#49f691 eyr:2026 hgt:179cm\n', '\n', 'byr:1925\n',
             'pid:555786686 hgt:189cm hcl:#cfa07d iyr:2012 ecl:gry eyr:2028\n', '\n', 'iyr:2016\n', 'hgt:168cm\n',
             'eyr:2027 cid:60 ecl:gry hcl:#cfa07d\n', 'pid:322944081 byr:1993\n', '\n', 'pid:163cm\n',
             'hgt:189cm iyr:1997 hcl:03db25 eyr:1970\n', 'byr:2016 ecl:#6c59eb\n', '\n', 'pid:766719295 iyr:2017\n',
             'hgt:168cm\n', 'hcl:z ecl:grt\n', 'eyr:2022 byr:2010\n', '\n',
             'hgt:173cm pid:247156751 cid:109 eyr:2022 iyr:2012 ecl:gry byr:1989\n', '\n', 'cid:288\n', 'hcl:77241f\n',
             'hgt:157cm byr:1956 pid:587115461 iyr:2016 ecl:lzr\n', 'eyr:2034\n', '\n', 'hcl:5307c9 ecl:#cc4aff\n',
             'pid:#d80d30\n', 'cid:224 hgt:72cm byr:2025 eyr:2039 iyr:2025\n', '\n', 'eyr:2027 byr:2015\n',
             'hgt:184 hcl:98fb9d pid:58151347\n', 'iyr:2029\n', '\n',
             'hgt:183cm cid:187 byr:2019 ecl:xry iyr:2013 pid:164cm hcl:#18171d eyr:2021']

    def __init__(self):
        for line in input:
            while line!='\n':



    def load_input():
        input_lines = []
        with open('./resources/input.txt') as file:
            input_lines = file.readlines()
        return input_lines
        #
        # count = 0
        # for line in lines:
        #     count += 1
        #     print(f'line {count}: {line}')

###
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
###