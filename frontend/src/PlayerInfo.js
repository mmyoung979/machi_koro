import React from 'react';

// Thsi is reusable component for all players who enter the game
const PlayerInfo = (props) => {
    return (
            <div className="player">
                <a href="/" className="avatar">
                    <img alt="avatar" src={props.avatar}/>
                </a>
                <div className="playerName">
                    <a href="/" className='userName'>
                        {props.userName}
                    </a>
                </div>
                <div className="metadata">
                    <span className="buildings">
                        {props.buildingType}
                    </span>
                </div>
                <div className="money">
                    {props.moneyAmount}
                </div>
            </div>
    )
}

export default PlayerInfo;