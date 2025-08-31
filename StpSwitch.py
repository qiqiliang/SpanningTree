"""
/*
 * Copyright © 2023 Georgia Institute of Technology (Georgia Tech). All Rights Reserved.
 * Template code for CS 6250 Computer Networks
 * Instructor: Maria Konte
 * Head TAs: Johann Lau, Erick Herring, and Ken Westdorp
 *
 * Georgia Tech asserts copyright ownership of this template and all derivative
 * works, including solutions to the projects assigned in this course. Students
 * and other users of this template code are advised not to share it with others
 * or to make it available on publicly viewable websites including repositories
 * such as GitHub and GitLab. This copyright statement should not be removed
 * or edited. Removing it will be considered an academic integrity issue.
 *
 * We do grant permission to share solutions privately with non-students such
 * as potential employers as long as this header remains in full. However,
 * sharing with other current or future students or using a medium to share
 * where the code is widely available on the internet is prohibited and
 * subject to being investigated as a GT honor code violation.
 * Please respect the intellectual ownership of the course materials
 * (including exam keys, project requirements, etc.) and do not distribute them
 * to anyone not enrolled in the class. Use of any previous semester course
 * materials, such as tests, quizzes, homework, projects, videos, and any other
 * coursework, is prohibited in this course.
 */
"""

# Spanning Tree Protocol project for GA Tech OMSCS CS-6250: Computer Networks
#
# Defines a Spanning Tree Switch that serves as the parent to the Switch class that is
# implemented by the student. It abstracts details of sending messages and verifying topologies.
#
# Copyright 2023 Vincent Hu
#           Based on prior work by Sean Donovan, Jared Scott, James Lohse, and Michael Brown

from Message import *


class StpSwitch(object):

    def __init__(self, idNum: int, topolink: object, neighbors: list):
        """
        switchID: int
            the ID of the switch (lowest value determines root and breaks ties)
        topology: Topology object
            a backlink to the Topology class.
            Used for sending messages: self.topology.send_message(message)
        links: list
            the list of switch IDs connected to this switch object
        """
        self.switchID = idNum
        self.topology = topolink
        self.links = neighbors

    # Invoked at initialization of topology of switches, this does NOT need to be invoked by student code.
    def verify_neighbors(self):
        """ Verify that all your neighbors have a backlink to you. """
        for neighbor in self.links:
            if self.switchID not in self.topology.switches[neighbor].links:
                raise Exception(f"{str(neighbor)} does not have link to {str(self.switchID)}")

    # Invoked at initialization of topology of switches, this does NOT need to be invoked by student code.
    def send_initial_messages(self):
        """ Sends all the initial messages.
                Called in Topology.run_spanning_tree()
        """
        for destinationID in self.links:
            self.send_message(
                Message(self.switchID, 0, self.switchID, destinationID, False, self.topology.ttl_limit)
            )

    # Wrapper for message passing to allow students from avoid using self.topology directly
    def send_message(self, message: Message):
        self.topology.send_message(message)

    def __str__(self):
        return (f"""Switch<switchID: {self.switchID}, links: {self.links}>""")
