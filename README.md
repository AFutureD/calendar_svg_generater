# calendar_svg_generater

Use php or python to generate a daily calendar svg. The python version support sererless.

## How to use

upload the `calendar.php` to a php server.

With the link `http://[YOUR_MOMAIN_OR_IP]/calendar`, you will get a svg.

<img src="./img/default.jpg" width="20%">.

## Parameters

With the link `http://[YOUR_MOMAIN_OR_IP]/calendar?highlight=false&date=2020-05-06&strip=false`, you will get a svg with defferent style.

<img src="./img/with_params.jpg" width="20%">.

`highlight`: The default value is `True`, the `day` text will be black. IF `False` or `false`, the `day` text will be gray.

`date`: Show today's date by default. You can give the value like: `tomorrow`, `next mon`, `2020/05/20`, `May 6, 2020` etc.

`strip`: The default value is `True`, the `day` text will shows without `0`. IF `False` or `false`, the `day` text will be show with `0`.


