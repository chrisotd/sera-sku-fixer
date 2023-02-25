# sera-sku-fixer
fixes and apends skus for sera systems parts hvac


Hi all, this may be way to deep but amight be useful to someone, someday. I'm the new guy, and I asked the question "why can't I search parts by sku?". "Haha, you just can't" wasn't the answer I hoped for, so I changed that.

I have to preface this with: I am not a programmer. I'm not a tech guy. I've been a truck driver for almost the past decade. This code is poorly written, uses extra calls (resources/page visits to the server/sera servers), and is nowhere near optimized.

I made a python script that searches a list you give it (filtered in excel to cut out the 10% we had with the sku already in the part/vend name), adds the sku to the end of the name, and then puts that new name in both part/vendor name fields. This makes skus searchable, and also fixes the few hundred parts that come up as "salesperson's name" when im trying to do parts list pricing updates.

it breaks if multiple parts have the same first 30 characters or so (example all our filters are "filter merv 8 hepa yadayada 20x25x1" and sera search cant dig that deep to find the 20x25x1 specifically, so it bugs out or repeats the same filter 10 times...and I cant be bothered to have this script search from anything other than left to right indexing ie:x=len("search string")/2, "search string"[x] instead...or something). It may break in other spots. It uses mostly hardcoded Xpaths that may or may not even work for your page/non hvac trade.

I wrote this like a month ago, and I hate coding pasionately...so I can try to help or guide someone ambitious or with similar goals. But no promises.


***originally posted in the sera systems facebook group***
