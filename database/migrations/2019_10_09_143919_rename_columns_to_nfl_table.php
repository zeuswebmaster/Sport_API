<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class RenameColumnsToNflTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('nfl', function (Blueprint $table) {
            $table->renameColumn('event_time', 'EventTime');
            $table->renameColumn('identifier', 'Identifier');
            $table->renameColumn('created_time', 'Created_Time');
            $table->renameColumn('updated_time', 'Updated_Time');
        });
        
        Schema::table('nfl', function (Blueprint $table) {
            DB::statement("ALTER TABLE `nfl` MODIFY `EventTime` varchar(50) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `Created_Time` varchar(30) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `Updated_Time` varchar(30) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `HomeScore` int(11) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `AwayScore` int(11) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `Identifier` varchar(100) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `HomeName` varchar(20) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `AwayName` varchar(20) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `GoogleMatch` varchar(10) DEFAULT NULL;");
            DB::statement("ALTER TABLE `nfl` MODIFY `GameStatus`varchar(15) DEFAULT NULL;");
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('nfl', function (Blueprint $table) {
            //
        });
    }
}
