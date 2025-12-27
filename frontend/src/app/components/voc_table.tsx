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
                    <th>English</th>
                    <th>French</th>
                </tr>
            </thead>
            <tbody>
                {vocList.map((voc, index) => (
                    <tr key={index}>
                        <td>{voc.word}</td>
                        <td>
                            <a
                                href={`https://de.pons.com/text-%C3%BCbersetzung/franz%C3%B6sisch-englisch?q=${voc.translation}`}
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                {voc.translation}
                            </a>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    )
}
