<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateNcaaTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('ncaa', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->string('EventTime', 50)->nullable();
            $table->string('HomeName', 20)->nullable();
            $table->integer('HomeScore')->nullable();
            $table->string('AwayName', 20)->nullable();
            $table->integer('AwayScore')->nullable();
            $table->string('GoogleMatch', 10)->nullable();
            $table->string('GameStatus', 15)->nullable();
            $table->string('Identifier', 100)->nullable();
            $table->string('Created_Time', 30)->nullable();
            $table->string('Updated_Time', 30)->nullable();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('ncaa');
    }
}
