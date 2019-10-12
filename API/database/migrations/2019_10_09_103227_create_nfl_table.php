<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateNflTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('nfl', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->text('event_time');
            $table->string('HomeName');
            $table->smallInteger('HomeScore');
            $table->string('AwayName');
            $table->smallInteger('AwayScore');
            $table->string('GoogleMatch');
            $table->string('GameStatus');
            $table->string('identifier');
            $table->text('created_time');
            $table->text('updated_time');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('nfl');
    }
}
