import React from 'react';

function PlayerDetails(props) {
    return (
        <div>
            <h1>{props.song.title}</h1>
        </div>
    );
}

export default PlayerDetails;
