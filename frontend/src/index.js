import React from 'react';
import ReactDOM from 'react-dom';
import PlayerInfo from './PlayerInfo';
import Player from './PlayerInfo';

const App = () => {
    return (
        <div className="ui container player">
            <PlayerInfo>
            avatar= 
            userName= Matt
            buildingType= Wheat Field
            moneyAmount= 80
            </PlayerInfo>
        </div>
    )
};

ReactDOM.render(<App />, document.querySelector('#root'));