import React from 'react';
import ReactDOM from 'react-dom';

const App = () => {
    return (
        <div className="ui container player">
            <div className="player">
                <a href="/" className="avatar">
                    <img alt="avatar" />
                </a>
                <div className="playerName">
                    <a href="/" className='userName'>userName</a>
                </div>
                <div className="metadata">
                    <span className="buildings">buildingType</span>
                </div>
                <div className="money">moneyAmount</div>
            </div>
        </div>
    )
};

ReactDOM.render(<App />, document.querySelector('#root'));