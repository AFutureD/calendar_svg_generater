<?php
    header('Content-Type: image/svg+xml');

    // Get date from url paramater
    $date = isset($_GET["date"]) ? strtotime($_GET["date"]): strtotime("now");
    // Get black state from url paramater and format to boolen
    $black = $_GET["highlight"] == "false" || $_GET["black"] == "False";
    // if not stripe off 0 from day
    $strip_flag = $_GET["strip"] == "false" || $_GET["black"] == "False";

    // forma date to String 
    $day = $strip_flag ? date("d", $date) : date("j", $date) ;
    $month = strtoupper(date("M", $date));
    $week = date("l", $date);
    $color = $black ? "#66757f" : "black";

    echo <<<EOT
    <svg xmlns="http://www.w3.org/2000/svg" aria-label="Calendar" role="img" viewBox="0 0 512 512">
        <path d="M512 455c0 32-25 57-57 57H57c-32 0-57-25-57-57V128c0-31 25-57 57-57h398c32 0 57 26 57 57z" fill="#e0e7ec" />
        <path d="M484 0h-47c2 4 4 9 4 14a28 28 0 1 1-53-14H124c3 4 4 9 4 14A28 28 0 1 1 75 0H28C13 0 0 13 0 28v157h512V28c0-15-13-28-28-28z" fill="#dd2f45" />
        <g fill="#f3aab9">
            <circle cx="470" cy="142" r="14" />
            <circle cx="470" cy="100" r="14" />
            <circle cx="427" cy="142" r="14" />
            <circle cx="427" cy="100" r="14" />
            <circle cx="384" cy="142" r="14" />
            <circle cx="384" cy="100" r="14" /></g>
        <text id="month" x="32" y="164" fill="#fff" font-family="monospace" font-size="140px" style="text-anchor: left">$month</text>
        <text id="day" x="256" y="400" fill="$color" font-family="monospace" font-size="256px" style="text-anchor: middle">$day</text>
        <text id="weekday" x="256" y="480" fill="#66757f" font-family="monospace" font-size="64px" style="text-anchor: middle">$week</text></svg>
    EOT;
?>