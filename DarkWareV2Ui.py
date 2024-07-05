import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog
import os
import pyperclip
import platform
import webbrowser
import subprocess
import win32api
import win32con

script_dir = os.path.dirname(__file__)

CORRECT_KEY1 = "PermFreeKeyForJob483gfjn54jkghnytuhsdk49gjkemf39jhfgdgdfgdg4g¤GRH&#¤E&%/&"
CORRECT_KEY2 = "@p0NVB}vtJ[\l^r0<]6Y'?A^&XV0$+C08pg%/E`:£2Yg,EnbD~!)k3Vwu_6GQCr0MCU/)N1S3eRLm`niKVovQ5fdsiojfui45jg954jgfiogj5yioutjmgfkhjmytoihjfkglhjt6iohjfiho"
CORRECT_KEY3 = "7UqUVmcRZjZTwXSBBMRK6V7gPYn3XYAf9dwU3oZQusNaGX6gjB2auKQjZdNQrWLnCdXyzSyqtw5pBxiJBPL4fSC2s3qfqzZT6g2d7JnRe9bdTvtxrtCWkkoAonRfhK7qoZvnQKSsBRmZfEZS3PHWCZwqVh7EoakRXQPfGuhN4kPxQAqkGrzTNKJWRru75LprbVFQyAfDcFN6GrYSkPVtJgwJqwugvc824vcf2dkaAAYrGww5LQ5AwLcenDSxTgvhSJDeuEt3dbhR#prSdwEyECRDpcV%qdPG@@*JeA4Ab$5$Z&kaoQwFrRocppemxotxspgenjDEQH7Bsqf5wxWoL^LKqKXS#g7cSZK6EQh$Kw!rTXtMdZXHXDzD@oC8EKQKgAFFpU9*BrZjSASaXhGy8Ci%H*33M&m3a*P4N6NjcY@g4sKhiuo&gm!sWc7VR$2B@NcWy3PU9#cMP8A@P7*fLX7%zCns&Wx4*B&6oaEYqkCz47d9dG5WMSrVZPXodqr6"
CORRECT_KEY4 = "54As@Y6pkDAFXwGMB#Uw7nexJkMcJ94Qg2aXzZAJXc69FBDCmaTGitd9df&oiVfoWWCcWXbtRW!xbysWKv8*maXHf&!zCibMkMp4wiAPq^#WiN^^ndPHvQwWowjVK&xM54As@Y6pkDAFXwGMB#Uw7nexJkMcJ94Qg2aXzZAJXc69FBDCmaTGitd9df&oiVfoWWCcWXbtRW!xbysWKv8*maXHf&!zCibMkMp4wiAPq^#WiN^^ndPHvQwWowjVK&xMPvZs8^iwEc@9mgP*ZnoSjGW69Ad2V8RzpAGoiXPaSHtADP$qeWZ6SYM#jwVDQUp@E^pjCFMriBsK3uTiXRcN9e8eY*X3%7qBhq332Z*vvoXWevaYwLBsrbX7sDQCQju$FPMffJzMoApSnmZeKkpcvDLkWKSLqt87QcgTi@JRgC9GkP^xvaAe^xHoXXmPDj5^Kt#xa7KQJZmwwc^t4B!erL3BrftX**efAn6m2huGDysK2HrM67qZ*CbnqaU9^Hd2RvThHtweSw^&km7PiTYyvbi*gm4avHiB4!SVL2GPaon8%ooMsoYBLmktBJAhaf2Dgw&zrCzvAyoxKJSSaEE&juQP^Mk6$CJpP9Uot9YXf$MuAsWLV*zoH%uE6*e$N$HCdPdT4hoZMAt9yPa%fpSCU3^Re&PVMbhXr#G$!p$hmNu@KvyL%vH58&J3Wkge6TRMoVnv4LS!7tH3j3xd88zDFhEQrC!6#!^8%%s%FV9dasoG3$3d&%s%*rQZCa94t#@pJou8iYW74SKhf33gNp7AvJwxUw@MGMMb!YqMroHCFoRxJey9fbg6$Mg7KFZ*WomYkXs&ryTKoYh4j!pQTkaVy^cCYMmUKnmPPDCF*4wqy@GEWrUWuj##tLBD9kJfuFrg"
CORRECT_KEY5 = "Qw^g9GvodSriCKJoQAXXvZ#cGwskpB2se!LL45#5Lb7%aLyx9mdPbSWW$cYE34gHPrW$T8HJX@%TCHepGT8upX8@v^W@N%aDNsYP&uJ3QEjRFE&zADRuGzqJGLKiwRXxuLxwht#JZFL6y^&xG3oo#$wgBYWJ98qxkJXtHgBJ@fW&iKCZKs7v5#Ra8gJS!K#KvhsVnhGDP8ow^Hjz7TH6Gy2y!ParvfAvr@b&dwpTUpoFMtv34EhwNCZB#P$zTR3@@yDS7bzhv#bpKxVqmFvkh@^!YUE%G%Y5zhzu4BuB!ubj6^ZqsHTfSWsT&7jWy95B9CM$Fte6Hu#xSYq%Qr3xiGXNBeXE&M5x2MBfZnGjr&@e&ZYD#z4ec#k2Tfe$&X2kWp@R$vWCreT35x%ZGttefZ%*66NPLPwXJ9Qh^YHiBg43Fow7jS5Ph@KkJranL7W76uZ^3ak!VUv8qjhsB^6iQF5Sdv$ZfxMmKNjE5Ym3W67*!YxXD^&uCPwz%^Xg84&R9VRzeGXkP$gyEVPVnLHD7&#&Qknk#izrkH$m#B#%3!gPeQgaW3w@%vAj49n3@*zgBcWGq3kxVRchj968KoLrNWAgi$NfoxLqgQR7$eSWzj5Wbap!6xpg^Ro832wYruRi8#k&z&ehtQoGioN#9uoYM!gzn&97^KmfP3snWQ7&fG2hqY2Q7J@rJjmNLZdsVVin*4VK!T&RPQpuZVZN!&qf9oPwzqdS3#fqCDR%q2BVVuD#5$npB3cdT32XiHSG9skbDdd58e2c&uLqKUw!n6SHzrzy$$76p%SdpVLQ&HR^trfyXihEdAji7%8r#qpeDpzDiQzJcZM#Xf6gy*cfY5H$PuAFV&N&&EQoJNMBR#QsvZ55!V9fA4Nu@WysGC#XjY8dKWj6rLhKvKKaBQ@7mdjFtGYW#WE!vrX83wzJUMscpXhF%mdt@WaMJ@mpr8B4BXa7oHER7mK6@GZbiVXAGyHd@&2EdG*rAojRUXw@A^qUzEuh7o8DJd#A5Rk4veHyAs3&"
CORRECT_KEY6 = "8HhdMV&p2H#bhF@*vAy5q^cu9hKzb^*mWuNo2!b#jpnEw6ejeEMnpVU%FqWAk3gxK9Zh7y8ex2UVW&dQJR@fKvz@@RSA%bQ$n4GY*HL9Z!Xkt%42@MrGiLDvWpPh@95tC2n5M!qSwaH5ypinga#CAiKfnA&oUpBVYoY#oaWBEQr6%Mp@CQg&#Sq6UkuZZfYDCQyKoV#T%NP6$GvS%&w62HKTesqoC#a@3&uzgreC*7!F4HjUsZE#yP*S@$faxmLiRD9hparp5Zhs&yJp&n!w7aL#YCtDktxiPya$S!4%F6k4HP^s5*Bwz$9FGeC2oHt!$Qiid!fcCxch7bMRrjRqym6TqN@QbBa9VbXb#pWuehWEKdMWg#h&ay28kmwTjH&32Fy3E3W&j278W%^4Ub*BL9uxbeXVDstvYgFnhR4pFM&f4W6&oKCUxo5k$YAc4U!E2T5UZQ8uf@p7BsfjaZnCPD2e2fR5fXwZu@^dp&!#6mAdVn6HYE6sZG*K7!%!9&8QPR$^A%2zwE9wjvogZMn9kFeaHYjj@p7NHKYKi%6jV@u^%DFJJ3G3Y6K^%tpQ7UA^9Q@inc*Uk2Dj^kvkk4G8^hmbRJRnnzGrwAn3RaUfkjPqK#oT7%7dJ5WAcGfb^#5z3iGckwQZDGe9D@HSCubMe&ZWFsPaq5R#dMb&WyPp8fseVgqn$quYgw6$9yaY!rxiw23zGn5fKE7c8vgewYvhQc2W^TkK3@fVfAKk@FP3xpe4dp2jvK&U#NLEno3FHD#%E$4nf9vbxm4u8yizYN!MGXJtf%a@&sc5rHtiwvEbcdG$fVY&NoG@sedtvE6BsYXpVFLG&sQJLsbBZU^D7SQ*q5NB8mfqPNoKs#KgtLCVkWnndYsprTYpBz5Q22E78aoetqKiPVZCg*#y54$WohxAUYvEe%RvEn2e3Rok29DzfxUw2sjSgfLm7mG78Y6mygHRmhA2@FRu8JKdpdzoWSYAuvsy$oaNZSE^xE%nNk4XRuWs7B8%pKrGaXAQcPS9cy^zB6zzy^txL#^uFq#i3MQb*NBZn4GJqjFUD^uv%#WChQHsWPC4Wr!R@$TY8P3BNrJ9e7TP6BNVE@mu6xEBc43%tKT44gqTNS!Fk^&$YmYAP3Y^hWhn23u&9rWg8NbaJ%A$#KL%JoRpRAD6xcGWqLTSoyrYEnp!8W&mPT8HC^Z!bc6a@hsfPXRdT&VYjZx2Y#m@J7dzF6gYfkw!m!pa!wJE3tHz$L8w!Logn!YmN$BtUAb%WuuE5Bhcst*NBJ^UF^7dXN$ChT5E@@Cvn4bfgYb4FpZ^RqRv7ZYr*N$Tp%f*8cBK4%SnRxZc%JD#%SRou**fPm8cBvsS&wztdjMYfd!dZWRjkgJu6Am9PZC9ADKRPvK6tkPn$KWeNe#TRYDoKoRbn&jt%S32sxbi6QmRuJDWT7VcM8KfGsAdT5XjvVzpg8@G*WM5%ffK9anMWfghvzVGES$Ae%6SLxHgyD*dsB82#MGV5mG$gukM6ctf3eQY9AP4Lii%nQ@26x#SehcfnKVDk^geUyJFbc&q3Pf*YRaC%Chn^TMsR@H6ZWrC%*96uwzDC$QYrXwbi#$EM3wR!bcm67twf!Gx^9$fPH*AVeS@jP@2y3&S9hgddZCTczBMgbMsd%&QBqmp*aL^C^@8@aHF@nK43&gS3bVrtWWNB&k88ZK6qWPUW52E4SnA7p$7#CdhoBvYqDah%ao%%C6jRo9mtWtLp*qH!fwY^E$NzB8s2cWbru4mxff$ogDJZuApsYGc79Vx9p&*J73ze*9gu%&b&k8*28Tt%@uBdCf%Xi8E&PDCkXaKdkybk%ea!n$Jz&fTku877suPvXi#n^MwZZ!juX$iuCE&a4ydrSCXoT3%$Gmy4jL^NSptXyxie^#FbSTLD6CtAbH5NJXr*Voq%h#V7jrR$Em!@bPEEmmLvEUdx@@nN7&uNQ@gbomYHEEsz!YEw55XraqHz9KsV&E6B&qqkSo^PgJeWU$YYbnr^Zk3oNt&Tub5Ee54FsNHs4j&BnmXj8TJ3ksM^7Q427WdJ!uYRCDvEdVe4EGc$V&%xvpSoEs$vP5KHJFrPZY4JqM$7Rek4qAeodQ#AN!Drn74wRhMo3eGwNp4TbcU86fJznG%^*eQPEiV4iqjU7WwaFkwbKgEzw$qBvSqG#HbZJnp48jFV7N8V52H48XSDbHVdm!C665fGp^t%&^#da9UQhiTGczXH98QfXP6bUN%tC*$wtSH^YGprK^o%*%woayQHLWmJhWFcg&dR$LyAx!h6WC*Y%ACMAioaMo2skRxic@c7qSuk5dXX$5UeG$KPthrz3wc^qzMWnF7pm#4yWGhzL5Wrs#DqFm7^8WDg#!a2WfGuaa7cZ$kJGACRt7Nk3rtJpskd!pWzotjQGtx4sU8xHUVsMtXH@3G2fY6TaprzEwTPwexgN!$VEzVQKM5Vm3wjfy^ZoWFt^aY5WdE68NYLtKumKxKF6X$J7!N86*!r!RL^5#V&4Doucxj*39YkWVbYSJ&fvj!C9!TuJR4Jn&kLVqWgN*FW7Tr27u&pUdXd9WAQYZA6H53rp!%DojnHEvxm*S*Fwhx6$Dbh3Xf*buvnDx8tfadAw&vMvB*xJja9W4HeHuW4fz&uST5g&ucpuJkFX!L3r&PLQCzRKXdVSZu#fbg*rJ6j6v%A24VMK@QJ@kG&Nab6sfQkpasQWBBGWoZTVYLmk5bG6rUme!5mJ%7uT@$Wc*&84o$YmZJtAJfkrdawhwTNscN#xGD9yWuCZehtWMwGc3E@7FA&cBhCUxsNS^FvmDD#yLEq3^T2RQv*AW!cMVrVHJSp37mwt!xuAHs97Xbz62JHyxTn4ZDw9uuRziRHxzfy%yqXvTzG%@prFa!CurL2px2#Su5*SLVF@Qg7E*jtp6UK@wjGDsKpX7se7R^rx36gdktcLjxF#ku&UGzdNF#B#Fm!wezC#xaLE!w3s&wH^brpLhkWPvNbiP*^jphM5r*Kw#gDMRW#%MS%WQz7toE4!i7%*o^%k%Se!X$^zFQU%MAa%wtPSJz%HSn6uqpdBw7z*mWK!Vm9RWg9TebaNqH6fc&o5rKzZEJSZbM5%n6wLVeopWCioyPfSqyE*DoWU9ap2FW&QFfoUzBvGSpDatJgaHhBYT32hWBx87$eTm9#QNmD7ZZiW7!LVYHu^MZTGnohkPdmGcQ2QgTbFgoGHc3"
CORRECT_KEY7 = "qd@#%Sjfj@r9HVV4yH!9s3jN#K*qsV8awqDRbjBkwAHmxiQevJPkiEac^wHxLe^ge^$wcofDLvpx8txXHba4fvvYQY5kApcp3ZzqRX$FhPu56$w8AbmWQHsUheKyjCz%Tvzo9yw^QwYbRGA5ZW@2qbqc*yEUZJdL6Zj@$QRQFqNF2QFYjGt^ecUcXRrKd^CR6v&sdFV&#6e6MrKe3T%jY!Qi2i8K2SkP%M4Ez8hUQuaqr!EHm&bNCe@e4qWiXJAJ^muXbWC77FK%F8!pThSobgd5wboT%f!SG!qnkXMQ9hWVe68WpypUs%^dcm5&rh%RnJ5&q&SUUrRnZiKGoY2Gx9cNpC4&Zjey3J*x9*xFGVYF8kC#Kc3iZ#4P8YTD5ahYA$Nu!Tz^Ry8yqMRNgM@LXN5uQsxHoGiXsf%JxBB!NvnypN$2YdzFNovg3MiyKxSzyiuBaZi9fTTykP&yeNdiN3uu^aHySd4zWj8G&PGoD!Vuhv2mF6xg%&&LmjZYsRhEwihYvgBhsWTvv^dP8jchkYNPgAYk3xwtKBLg97vR3exKXrasTh*txVPGR3x&BfR$3k2$UCK!YoZ%kX3fS6**%ik&riv4LP%*cNP6MwmF8#SrM&wctHPC9!5P!%yUMKVXAdai2jMa4Tf$aCL93b*&9TBuTCP3SirqKUm*G3L!BLeHd&gzXK$wnVcKNhv&Ao%M!kJEZSH8XyuRwvpykXS@!A$SvC&ESkze#ounEH3svPzHEhk9c2z*pNr&6VBULLMTN6hF2cKmr^k!g7sqA&z3GxmeMQZqxUQQ9RjNWTfrkha*9JZBtdqMBZP$zr6u4trnhi!49FrSJK$Q&xMHa2pYQ5HU*KMuYHgho84cP&AKmNjRb7vi#pReB3#eZj7HWnT$A5DKnm*9qzYokLM%bi9tWc6BtAQYi7P37VSEeZNzzW5ea7^j*XL*dXxwmb3qTK#UXqh#*HHAj4xHmt3a2@HwBqT3pyPYnMkBFEE^Mmk2A$E2yAyFrVjx2AskB7rnFjy$Dnkx!o$H9@YeE^6XG$Z&g&FDCZsuwjyD8v&7pmiPtitBSFTGsFsY%3zP^n5YJ2KV7BFiAQ$Y&4QLKrpYpRqNMy5tuEh$SBsTM@3fnjbz&vv9U5W&Dtn&rB$uCDk8&D6J$&xmfP4h&ww&YcCXBL#7%D$zs62KEWFvAG8ubKz#nJ@BJmPQtaH5oa7mWmWSUv8oCaGL#vzWwsescp*SkL5t6Y7Q^8w%g7EpAjiFDsPm6$UEjQ&B@G6&ajuJqC$uvnksFAe5@zG#kYB5n!Fo$dF4N@3k25U6eu9&r5H@DE*UB&gmTLoTBi!xQRE4fseQTsW@DbyzWAaZrKgJ*QwVn34!8@N4AX#U4dd6byvXjNEEiWsUxKkJBuV#amLZUF5CDfoCijoMMtyn9%rS!k@wTfZ^A^r!S6jX*fC!fpk5JauKZXh4HTGJtibgN*C&@FDoQaiP$pu34ovfFYzXXys7G3rna7BjW8Dt*pTtW3KKCxhX928zrjH&gSeCci8K*gJ!RhYsBssAb!$LhyFUaRABgTd^Xw#Rh6ptQbvMcbC$9UE7AvEr8HPfnT9akFCiKC@bbrgAFk^rSqS*jYNZmhHXHG$WWjhZ6HtT7PGD2^5uewQ7J*%^Wkt3HFPzD#DiN7JFAL2rgWUCxHNLFdDT!8Ng%@vFp!Cf@$hjSw&WFEj@it!Kb6Sw4TQT5%EWJCgQP%D3L3hJY#8&YumPDCPVg8h4PJmSPxxUhpiQA#gzMBKU!EuzXQjTiLj44Yt2Et^J8edp8&M3!ZCsKY77GA5no7LAZR6a$Vh&avE$$KwKBRTnSU7mgzxABcjpg&3Ly6Zre&phFF$x*xZRkDAJQjuJ3aF%FAGspJiUQs3k*^!5!hgSWTUunjQCZGuy@n$HkVEmW#t3@G7%VTnNq36RGGykA8AfYmQ2SXRx8uqcaYJhBy^q4dEZv8mc7NkvCwzwTKuSssy#$q%Zv^pLhVg*EL7uzn^7^WCoGsMNNLKW8nkg9UBZvNjFY%i5jY^QGk$#g3B63eniM*mfJrx4F#wrdipR#rzW6vCHTrD&q6eJGE*pnQAkghDZpE@#zwcfGpC$YW*VzP*MS!q2@C$XV8UMZa8E%!R#M%9p$bZ2TCWwfo2VUXVN*piH$kJ@uQ*JkF4PzrQkQ*hD9iuk6yFQUCBRonPAA5&VV9!8V!8gfXVaPZopVmKzbLtsEUg*a^cbirR5iUpzi5ZnEuuzuwiZVWTSCEJoV9Rebwz6MQTaRZL@Pr5rMUcE38XhvYUE#^36M4U^RPdMm$Z!v3FnNYWBPRyKXuhCJrT*3Q#aEM7h&hxoynTn@#Qh5^xUz#fAifFtpzdKJs!Zg7E^Zir$pTE#@jDcGpWzg8t%vVZX3qhUMqF$@UUy3u9!EV$AcP!boY4jfCHun$Xh#@B@nimyjXGGueZ*riqBnr9tk5zHwTiRh2RS^YAS$CAo!ebjuicCoz@tSBt#PxDg2D%$ArzkMBGor64CRPJwWYeBJrdgFHMsuqaT5aciEZBY!G^6L9L9zBV@XC@SBGMXfo2$Yh$CjXGGueZ*riqBnr9tk5zHwTiRh2RS^YAS$CAo!ebjuicCoz@tSBt#PxDg2D%$ArzkMBGor64CRPJwWYeBJrdgFHMsuqaT5aciEZBY!G^6L9L9zBV@XC@SBGMXfo2$Yh$CjXGGueZ*riqBnr9tk5zHwTiRh2RS^YAS$CAo!ebjuicCoz@tSBt#PxDg2D%$ArzkMBGor64CRPJwWYeBJrdgFHMsuqaT5aciEZBY!G^6L9L9zBV@XC@SBGMXfo2$Yh$CjXGGueZ*riqBnr9tk5zHwTiRh2RS^YAS$CAo!ebjuicCoz@tSBt#PxDg2D%$ArzkMBGor64CRPJwWYeBJrdgFHMsuqaT5aciEZBY!G^6L9L9zBV@XC@SBGMXfo2$Yh$C"
CORRECT_KEY8 = "H$r3$y!d^ueD4wz7gS*gKVoC6#wxr8b4jT5V7Y3^kLLV52MjRPd4v3GP8j8q&rQrqsiTH!s#7yca&!wGMRVfBRBS#ETXW3Kyo$ifT3pPi$QVXg7P4K%RmJe85@qEbK5qH$r3$y!d^ueD4wz7gS*gKVoC6#wxr8b4jT5V7Y3^kLLV52MjRPd4v3GP8j8q&rQrqsiTH!s#7yca&!wGMRVfBRBS#ETXW3Kyo$ifT3pPi$QVXg7P4K%RmJe85@H$r3$y!d^ueD4wz7gS*gKVoC6#wxr8b4jT5V7Y3^kLLV52MjRPd4v3GP8j8q&rQrqsiTH!s#7yca&!wGMRVfBRBS#ETXW3Kyo$ifT3pPi$QVXg7P4K%RmJe85@qEbK5qH$r3$y!d^ueD4wz7gS*gKVoC6#wxr8b4jT5V7Y3^kLLV52MjRPd4v3GP8j8q&rQrqsiTH!s#7yca&!wGMRVfBRBS#ETXW3Kyo$ifT3pPi$QVXg7P4K%RmJe85@qEbK5qNWE2BYU4eoocG#cwVMdZ!!FF&SHq3J!!2tDfe#Q9h#9mqy6QVfBmvgvE6cveuiuT!qGg$hhjZrujZ%Xj#ufi9grHNwmhpy%H@fKatV4*#zT%XfQ%VzUhSXRXS*H^TwBSNWE2BYU4eoocG#cwVMdZ!!FF&SHq3J!!2tDfe#Q9h#9mqy6QVfBmvgvE6cveuiuT!qGg$hhjZrujZ%Xj#ufi9grHNwmhpy%H@fKatV4*#zT%XfQ%VzUhSXRXS*H^TwBSA4noA^veE5x#RCqVDDVFcGNa2wNfUHXkziq^WKWe95LUU7RJoUP!rvNfgs94J6XdwP#kkc28Tp&wexRQmajSaY##A75#FswwvTuhoLTsas$tysJBS7u6n%^4Hjuyu4fjA4noA^veE5x#RCqVDDVFcGNa2wNfUHXkziq^WKWe95LUU7RJoUP!rvNfgs94J6XdwP#kkc28Tp&wexRQmajSaY##A75#FswwvTuhoLTsas$tysJBS7u6n%^4Hjuyu4fjeEXEA5LgpZNbCTHv7qVbZ9txg85FivYLNdp$L9nWG7#h%2iX4vUyy@!jdjMstCDr!zKA8@f5%t&Ddn7s%estXZni72QBXY%&EjQj!W$jmFaSetoY25*BK#fLkRu9VtEjeEXEA5LgpZNbCTHv7qVbZ9txg85FivYLNdp$L9nWG7#h%2iX4vUyy@!jdjMstCDr!zKA8@f5%t&Ddn7s%estXZni72QBXY%&EjQj!W$jmFaSetoY25*BK#fLkRu9VtEjcPeArjSAi7EU*py@%eZyGipvn2$9XVKhkyyq$UfY$e5VFQ5%asi9fZq%UAWxmN@a4g!d5*idhDkgh@&P&Mezpk@&6husqdqXbJ6qdzYTAaUAgtnp#yD*5UNh5jHiJ!HrcPeArjSAi7EU*py@%eZyGipvn2$9XVKhkyyq$UfY$e5VFQ5%asi9fZq%UAWxmN@a4g!d5*idhDkgh@&P&Mezpk@&6husqdqXbJ6qdzYTAaUAgtnp#yD*5UNh5jHiJ!HrDm!$kFG!4y!r*885HrdSt9pa9SET9AgY2xFhXJ4p#&9XQwvQ3UEFQbcNXbmyt#w4Be4^BH#&EHyjBs%LRjxnqhK63d4nP2MYjaEJ%PAF8cgfGX8!XLqYeoLoZ9*igT2HDm!$kFG!4y!r*885HrdSt9pa9SET9AgY2xFhXJ4p#&9XQwvQ3UEFQbcNXbmyt#w4Be4^BH#&EHyjBs%LRjxnqhK63d4nP2MYjaEJ%PAF8cgfGX8!XLqYeoLoZ9*igT2HNnjeYjMKSR6GgL62gGP48qRPh@rsB8zub5XbYHBaW$qMuJUM!U@^RE8^ZGyzv6rPA5K2owNsqsvwJJmdY4#piirhciHr@!%DHmZsuS5hazK!gvdspBAyHqiycxyF^kLnNnjeYjMKSR6GgL62gGP48qRPh@rsB8zub5XbYHBaW$qMuJUM!U@^RE8^ZGyzv6rPA5K2owNsqsvwJJmdY4#piirhciHr@!%DHmZsuS5hazK!gvdspBAyHqiycxyF^kLnZfr4jGCw*@FDmN38hUTXZRv!xk*7FQdVh!bWw5CVv!RTDvh$@c36Pa^j@m#wYah&Atv3GFZmJVij^jE8#8T2WrRAS5TfckQzNcv6f7uNM8XB!Pc2Ph!7ru$N^dPHRm@4Zfr4jGCw*@FDmN38hUTXZRv!xk*7FQdVh!bWw5CVv!RTDvh$@c36Pa^j@m#wYah&Atv3GFZmJVij^jE8#8T2WrRAS5TfckQzNcv6f7uNM8XB!Pc2Ph!7ru$N^dPHRm@4"
CORRECT_KEY11 = "HJWZg^LsxK%Jk#gWm^qT89bKth5qFAuDQFDZH97Zu**8oMRhKChh8eXeD!vYNwVu%wxrGW3nHBpeMrpzv&XYB#hN$TPF$VM!2PL22#w4PuNwuWP42SBbmvN66@TtseWCpg&Mrb!&Fzvd&QYUoVKL@yUn6AF@G4x5E4oV4R^tX%E2x7*ctPwYiBe#@xeZ#rTY^F4nc2BUrAQF2AsEGyjotbkqqt6LaU&%cbt$ZZ8@nzHGosYiS36^YyLm2wP^p5V2TjbNcFFM5W3doc&9iEUjyMB6h$v7dfP3JzYLrEtJ$6zyfDHndneF3^meMf*%ZVLBPD#zbtT6zNt4*KBYyBepfAH5W#W^syDXkj87@qknPvyZpTdoY$$rr473VaTzUL65@NkFYkUeJ5AK&Y%AjC@ZoAEKSzDKGsqH4H9Ga6LQ4*kteRUh3uq6NCdH%$DdmwrE^zNTJ7uGrP%JhDFXd^BPy5#anviFfA4g#UtnCa5uba!MfbMHe@mZA%YYd^9iFCsf6oueuntiofxwhb5b39ekqyc*hXYoBZd*^bbfMcvrr%bFFF#qFm4t^z@4ce2g&Kh5fhcce*q7Socc$Y@FPg9VCv9q$d93Qs@K*S&59mFVLN#h^^6XKykJf5mEcGBHWki&TK&BTQF&K6RpU9M95X62mCbw7^n@nH3wdn@CWYEjaWmnLkeT3$zZqMGCSP9SQoWnk!9pjP#3tqeqvsRPBA#UcmveZ$WZqwDtH2Q5uwFikbKaaYF84oFU#U*%g3q&#ZqW"
PREMIUM_KEY = "GiftedByOwnerKey"

# Initial state of topmost (0 = off, 1 = on)
topmost_enabled = 0
premium_enabled = False

def validate_key():
    entered_key = key_entry.get().strip()
    if entered_key in [CORRECT_KEY1, CORRECT_KEY2, CORRECT_KEY3, CORRECT_KEY4, CORRECT_KEY5, CORRECT_KEY6, CORRECT_KEY7, CORRECT_KEY8, CORRECT_KEY11, PREMIUM_KEY]:
        messagebox.showinfo("Success", "Key is valid.")
        key_entry.delete(0, tk.END)
        show_main_window(entered_key == PREMIUM_KEY)
    else:
        messagebox.showerror("Error", "Invalid key.")

def copy_key_link():
    link = "https://raw.githubusercontent.com/DarkWareV2/DarkWareV2Scripts/main/FreeKeys/ChooseKey.txt"
    pyperclip.copy(link)
    messagebox.showinfo("Copied", "Key link copied to clipboard.")

def check_windows_version():
    try:
        product_info = win32api.GetVersionEx()
        major_version = product_info[0]
        minor_version = product_info[1]
        build_number = product_info[2]
        platform_id = product_info[3]
        csd_version = product_info[4]

        # Check if it's Windows 10 or 11
        if (major_version == 10 and build_number >= 22000) or (major_version == 11):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking Windows version: {e}")
        return False

def open_buy_link():
    buy_link = "https://www.productkeys.com/product/windows-11-professional-retail/?utm_source=Google%20Shopping&utm_campaign=ProductKeys-GoogleFeed-DK&utm_medium=cpc&utm_term=5041&gad_source=1&gclid=Cj0KCQjw7ZO0BhDYARIsAFttkChb_QtB3x6Yteomf5_lD35Y0SPBWAqUMFc13U4iTHv8nOBwNlsXZYgaAhgQEALw_wcB"
    webbrowser.open(buy_link)

def toggle_topmost():
    global topmost_enabled
    if topmost_enabled == 1:
        root.attributes("-topmost", 0)  # Disable topmost
        topmost_enabled = 0
    else:
        root.attributes("-topmost", 1)  # Enable topmost
        topmost_enabled = 1

def toggle_topmost_with_key():
    global premium_enabled
    entered_key = simpledialog.askstring("Enter Premium Key", "Enter Premium key to enable topmost:")
    if entered_key == PREMIUM_KEY:
        toggle_topmost()
        premium_enabled = True
        apply_rainbow_outline(canvas, outline_rect_main)
        apply_rainbow_outline(canvas, outline_rect_textbox)
    else:
        messagebox.showerror("Invalid Key", "Premium key is incorrect.")

def inject_button_click():
    if check_windows_version():
        injector_path = os.path.join(script_dir, "Injector", "DarkWareV2Injector.exe")
        if os.path.exists(injector_path):
            subprocess.run(injector_path, check=True)
        else:
            messagebox.showerror("Error", "Injector executable not found.")
    else:
        response = messagebox.askquestion("Need Windows Pro Version", "You need a Windows Pro version. Would you like to buy it?")
        if response == "yes":
            open_buy_link()

def show_main_window(is_premium):
    global premium_enabled, outline_rect_main, outline_rect_textbox, canvas
    premium_enabled = is_premium

    key_frame.pack_forget()
    main_frame.pack(fill=tk.BOTH, expand=True)

    image_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Background.png")
    if os.path.exists(image_path):
        image = PhotoImage(file=image_path)
        image_width = image.width()
        image_height = image.height()

        root.geometry(f"{image_width}x{image_height}")

        canvas = tk.Canvas(main_frame, width=image_width, height=image_height, highlightthickness=0)
        canvas.pack()

        canvas.create_image(0, 0, anchor='nw', image=image)
        main_frame.image = image

        # Create a text box in the center of the main window
        text_box = tk.Text(main_frame, bd=5, font=('Arial', 12), foreground='black', background='white', wrap=tk.WORD)
        text_box.config(state=tk.NORMAL)  # Make the text box editable
        text_box_width = 300
        text_box_height = 200
        text_box_x = (image_width - text_box_width) // 2
        text_box_y = (image_height - text_box_height) // 2
        canvas.create_window(text_box_x, text_box_y, anchor='nw', width=text_box_width, height=text_box_height, window=text_box)

        # Main window rainbow outline
        outline_rect_main = canvas.create_rectangle(0, 0, image_width, image_height, width=10, outline='')

        # Text box rainbow outline
        outline_rect_textbox = canvas.create_rectangle(text_box_x, text_box_y, text_box_x + text_box_width, text_box_y + text_box_height, width=10, outline='')

        if is_premium:
            apply_rainbow_outline(canvas, outline_rect_main)
            apply_rainbow_outline(canvas, outline_rect_textbox)

        # Function to handle window dragging
        def start_drag(event):
            global x, y
            x = event.x
            y = event.y

        def drag_window(event):
            x_new = event.x_root - x
            y_new = event.y_root - y
            root.geometry(f"+{x_new}+{y_new}")

        canvas.bind("<ButtonPress-1>", start_drag)
        canvas.bind("<B1-Motion>", drag_window)

        # Create buttons
        button_margin = 10

        exit_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2ExitButton.png")
        if os.path.exists(exit_button_path):
            exit_button_image = PhotoImage(file=exit_button_path)
            exit_button = tk.Button(main_frame, image=exit_button_image, bd=0, highlightthickness=0, command=close_window)
            exit_button.image = exit_button_image
            canvas.create_window(image_width - exit_button_image.width() - button_margin, button_margin, anchor='nw', window=exit_button)

        injector_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2InjectorButton.png")
        if os.path.exists(injector_button_path):
            injector_button_image = PhotoImage(file=injector_button_path)
            injector_button = tk.Button(main_frame, image=injector_button_image, bd=0, highlightthickness=0, command=inject_button_click)
            injector_button.image = injector_button_image
            canvas.create_window(button_margin, image_height - injector_button_image.height() - button_margin, anchor='nw', window=injector_button)

        settings_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2SettingsButton.png")
        if os.path.exists(settings_button_path):
            settings_button_image = PhotoImage(file=settings_button_path)
            settings_button = tk.Button(main_frame, image=settings_button_image, bd=0, highlightthickness=0, command=open_settings_window)
            settings_button.image = settings_button_image
            canvas.create_window(image_width - settings_button_image.width() - button_margin, image_height - settings_button_image.height() - button_margin, anchor='nw', window=settings_button)

        root.mainloop()
    else:
        print(f"Error: The image 'DarkWareV2Background.png' does not exist in the directory '{script_dir}'.")

def apply_rainbow_outline(canvas, outline_rect):
    colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]
    color_index = 0

    def update_outline_color():
        nonlocal color_index
        current_color = colors[color_index]
        next_color = colors[(color_index + 1) % len(colors)]
        color_index = (color_index + 1) % len(colors)
        blend_colors_smoothly(current_color, next_color, 0)

    def blend_colors_smoothly(color1, color2, step):
        def blend(color1, color2, ratio):
            r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:], 16)
            r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:], 16)

            r = int(r1 * (1 - ratio) + r2 * ratio)
            g = int(g1 * (1 - ratio) + g2 * ratio)
            b = int(b1 * (1 - ratio) + b2 * ratio)

            return f"#{r:02x}{g:02x}{b:02x}"

        if step > 10:
            return

        blend_color = blend(color1, color2, step / 10)
        canvas.itemconfig(outline_rect, outline=blend_color)
        root.after(50, blend_colors_smoothly, color1, color2, step + 1)

        if step == 10:
            root.after(200, update_outline_color)

    update_outline_color()

def open_settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("400x300")

    settings_background_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2SettingsBackground.png")
    if os.path.exists(settings_background_path):
        settings_background_image = PhotoImage(file=settings_background_path)
        settings_background_label = tk.Label(settings_window, image=settings_background_image)
        settings_background_label.pack(fill=tk.BOTH, expand=True)

        toggle_topmost_button = tk.Button(settings_window, text="Toggle Topmost", font=('Arial', 14), command=toggle_topmost_with_key)
        toggle_topmost_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    else:
        print(f"Error: The settings background image 'DarkWareV2SettingsBackground.png' does not exist in the directory '{script_dir}'.")

def close_window():
    root.destroy()

root = tk.Tk()
root.overrideredirect(True)

key_frame = tk.Frame(root)
key_frame.pack(fill=tk.BOTH, expand=True)

main_frame = tk.Frame(root)

key_entry = tk.Entry(key_frame, bd=5, font=('Arial', 14), foreground='black')
key_entry.pack(pady=20, side=tk.LEFT, padx=10)

validate_button = tk.Button(key_frame, text="Check Key", font=('Arial', 14), command=validate_key)
validate_button.pack(pady=20, side=tk.LEFT, padx=10)

copy_link_button = tk.Button(key_frame, text="Copy Key Link", font=('Arial', 14), command=copy_key_link)
copy_link_button.pack(pady=20, side=tk.LEFT, padx=10)

root.mainloop()
