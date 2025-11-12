import React from "react";
import { Vocable } from "@/app/schemas/vocables";
import "./voc_table.css";

type VocTableProps = {
    vocList: Vocable[];
}

export default function VocTable(
    { vocList }: VocTableProps
) {
    return (
        <table>
            <thead>
                <tr>
                    <th>German</th>
                    <th>French</th>
                </tr>
            </thead>
            <tbody>
                {vocList.map((voc, index) => (
                    <tr key={index}>
                        <td>{voc.word}</td>
                        <td>{voc.translation}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    )
}
