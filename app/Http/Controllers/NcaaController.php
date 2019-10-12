<?php

namespace App\Http\Controllers;
use App\Ncaa;

class NcaaController extends Controller
{
    public function show() {
        $ncaa_all = Ncaa::all();
        $data = [];
        $i = 0;
        foreach ($ncaa_all as $nfl) {
            $data[$i]['event-time'] = $nfl['EventTime'];
            $data[$i]['home-name'] = $nfl['HomeName'];
            $data[$i]['home-score'] = $nfl['HomeScore'];
            $data[$i]['away-name'] = $nfl['AwayName'];
            $data[$i]['away-score'] = $nfl['AwayScore'];
            $data[$i]['google-matching'] = $nfl['GoogleMatch'];
            $data[$i]['game-status'] = $nfl['GameStatus'];
            $data[$i]['identifier'] = $nfl['Identifier'];
            $data[$i]['create-time'] = $nfl['Created_Time'];
            $data[$i]['update-time'] = $nfl['Updated_Time'];
            $i++;
        }
        
        return response()->json([
            'status' => 'success', 
            'total' => $ncaa_all->count(),
            'data' => $data
        ], 200);
    }
}
