<?php

use Illuminate\Database\Seeder;

class NflTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $now = date('Y-m-d H:i:s');
        $timeval = time();

        $nfl_table_module = array (

            array (
                "event-time" => "2019/2020.04.10. 10:20",
                "home-name" => "Seattle Seahawks",
                "home-score" => "30",
                "away-name" => "Los Angeles Rams",
                "away-score" => "29",
                "google-matching" => "True",
                "game-status" => "Final",
                "indentifier" => "fb29b6501f465ab4b7e0ecf94ab6027c",
                "create-time" => "2019-10-04 23:59:17.003213",
                "update-time" => ""
              ),
              array (
                "event-time" => "2019/2020.01.10. 10:15",
                "home-name" => "Pittsburgh Steelers",
                "home-score" => "27",
                "away-name"=> "Cincinnati Bengals",
                "away-score"=> "3",
                "google-matching"=> "True",
                "game-status"=> "Final",
                "indentifier"=> "fe086a85d050bcaad947740924f716f1",
                "create-time" => "2019-10-04 23:59:24.831840",
                "update-time" => ""
              ),
              array (
                "event-time" => "2019/2020.30.09. 10:20",
                "home-name"=> "New Orleans Saints",
                "home-score"=> "12",
                "away-name"=> "Dallas Cowboys",
                "away-score"=> "10",
                "google-matching"=> "True",
                "game-status"=> "Final",
                "indentifier"=> "bbf3d515d9842a461aaeb455c76b6b47",
                "create-time"=> "2019-10-04 23:59:32.530252",
                "update-time"=> ""
              ),
              array (
                "event-time"=> "2019/2020.30.09. 06:25",
                "home-name"=> "Chicago Bears",
                "home-score"=> "16",
                "away-name"=> "Minnesota Vikings",
                "away-score"=> "6",
                "google-matching"=> "True",
                "game-status"=> "Final",
                "indentifier"=> "ee1d41d5407f75cc2eff21609f1e0afa",
                "create-time"=> "2019-10-04 23:59:40.054159",
                "update-time"=> ""
              ),
              array (
                "event-time"=> "2019/2020.30.09. 06:25",
                "home-name"=> "Denver Broncos",
                "home-score"=> "24",
                "away-name"=> "Jacksonville Jaguars",
                "away-score"=> "26",
                "google-matching"=> "True",
                "game-status"=> "Final",
                "indentifier"=> "e9792427f3bace786c2678f4769cf047",
                "create-time"=> "2019-10-04 23:59:48.124217",
                "update-time"=> ""
              ),
              array (
                "event-time" => "2019/2020.30.09. 06:05",
                "home-name" => "Arizona Cardinals",
                "home-score" =>"10",
                "away-name" => "Seattle Seahawks",
                "away-score" => "27",
                "google-matching" => "True",
                "game-status" => "Final",
                "indentifier" => "4d239c1bb809c451c9c299800e557866",
                "create-time" => "2019-10-04 23:59:55.266698",
                "update-time" => ""
              ),
            array (
                "event-time" => "2019/2020.09.08. 09:00",
                "home-name" => "Buffalo Bills",
                "home-score" => "24",
                "away-name" => "Indianapolis Colts",
                "away-score"=> "16",
                "google-matching"=> "True",
                "game-status"=> "Final",
                "indentifier"=> "426fd0decffc1990d6fe7a2a9fd25f2e",
                "create-time" => "2019-10-05 00:14:35.779652",
                "update-time"=> ""
            ),
) ;
    foreach ($nfl_table_module as $nflId => $nfl) {
        DB::table('nfl')->insert(array(
            'event_time' => $nfl['event-time'],
            'HomeName' => $nfl['home-name'],
            'HomeScore' => $nfl['home-score'],
            'AwayName' => $nfl['away-name'],
            'AwayScore' => $nfl['away-score'],
            'GoogleMatch' => $nfl['google-matching'],
            'GameStatus' => $nfl['game-status'],
            'identifier' => $nfl['indentifier'],
            'created_time' => $nfl['create-time'],
            'updated_time' => $nfl['update-time'],
        ));
    }

    }
}
